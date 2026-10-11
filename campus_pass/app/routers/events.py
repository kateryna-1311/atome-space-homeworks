from app.models.events import Event, EventCreate, EventUpdate, Participant, ParticipantCreate
from fastapi import APIRouter, HTTPException, status

from ._detail.json import database_lock, read_json, write_json

router = APIRouter(tags=["Events"])


def _find_event(events, event_id):
    for event in events:
        if event["id"] == event_id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Подію не знайдено"
    )


@router.get("/api/events", response_model=list[Event])
def get_events():
    with database_lock:
        return read_json()["events"]


@router.post("/api/events", response_model=Event, status_code=status.HTTP_201_CREATED)
def create_event(payload: EventCreate) -> Event:
    with database_lock:
        data = read_json()
        new_event = Event(
            id=len(data["events"]) + 1, participants=[], **payload.model_dump()
        )
        data["events"].append(new_event.model_dump(mode="json"))
        write_json(data)
        return new_event


@router.get("/api/events/{event_id}", response_model=Event)
def get_event(event_id: int):
    with database_lock:
        data = read_json()
        event = _find_event(data["events"], event_id)
        return event


@router.post(
    "/api/events/{event_id}/participants",
    response_model=Participant,
    status_code=status.HTTP_201_CREATED,
)
def register_participant(event_id: int, payload: ParticipantCreate) -> Participant:
    with database_lock:
        data = read_json()
        event = _find_event(data["events"], event_id)
        if len(event["participants"]) >= event["capacity"]:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Немає вільних місць на івенті",
            )
        new_id = max([pl["id"] for pl in event["participants"]], default=0) + 1
        new_participant = Participant(id=new_id, **payload.model_dump())
        event["participants"].append(new_participant.model_dump(mode="json"))
        write_json(data)
        return new_participant


@router.get("/api/events/{event_id}/participants", response_model=list[Participant])
def get_participants(event_id: int):
    with database_lock:
        data = read_json()
        event = _find_event(data["events"], event_id)
        return event["participants"]


@router.delete(
    "/api/events/{event_id}/participants/{participant_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_participant(event_id: int, participant_id: int):
    with database_lock:
        data = read_json()
        event = _find_event(data["events"], event_id)
        participant_idx = None
        for idx, pl in enumerate(event["participants"]):
            if pl["id"] == participant_id:
                participant_idx = idx
                break
        if participant_idx is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Учасника не знацдено"
            )
        event["participants"].pop(participant_idx)
        write_json(data)
        return None


@router.patch(
    "/api/events/{event_id}", response_model=Event, status_code=status.HTTP_200_OK
)
def update_event(event_id: int, payload: EventUpdate) -> Event:
    with database_lock:
        data = read_json()
        event = _find_event(data["events"], event_id)
        update_data = payload.model_dump(mode="json", exclude_unset=True)
        if "capacity" in update_data:
            if update_data["capacity"] < len(event["participants"]):
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Кількість учасників не може бути меншоюза поточну",
                )
        for key, value in update_data.items():
            event[key] = value
        write_json(data)
        return event
