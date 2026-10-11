from app.routers.events import router as events_router
from fastapi import FastAPI

app = FastAPI(title="Campus Pass API")

app.include_router(events_router)
