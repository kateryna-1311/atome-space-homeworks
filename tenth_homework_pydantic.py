from pydantic import BaseModel, field_validator, model_validator


class Passenger(BaseModel):
    first_name: str
    last_name: str
    age: int

    @field_validator("age")
    def validate_age(cls, value: int) -> int:
        if value < 0 or value > 120:
            raise ValueError("Wrong value. Enter age in the range 0 to 120.")
        return value

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Flight(BaseModel):
    flight_number: str
    origin: str
    destination: str
    price: float

    @field_validator("price")
    def validate_price(cls, value: float) -> float:
        if value < 0:
            raise ValueError("Wrong value. Price must be more than 0.")
        return value

    @model_validator(mode="after")
    def check_routes_match(self):
        if self.origin == self.destination:
            raise ValueError("Wrong value. Origin and destination must be different.")
        return self

    @property
    def route(self) -> str:
        return f"{self.origin} -> {self.destination}"


class Ticket(BaseModel):
    passenger: Passenger
    flight: Flight
    seat_number: int
    has_baggage: bool = False

    @field_validator("seat_number")
    def validate_seat_number(cls, value: int) -> int:
        if value < 1 or value > 200:
            raise ValueError("Wrong value. Enter seat_number in the range 1 to 200.")
        return value

    @property
    def total_price(self) -> float:
        if self.has_baggage:
            return self.flight.price + 50.0
        return self.flight.price


ticket = Ticket(
    passenger={"first_name": "John", "last_name": "Doe", "age": 25},
    flight={
        "flight_number": "PS101",
        "origin": "KBP",
        "destination": "WAW",
        "price": 2500,
    },
    seat_number=14,
    has_baggage=True,
)
ticket1 = Ticket(
    passenger={"first_name": "John", "last_name": "Doe", "age": -4},
    flight={
        "flight_number": "PS101",
        "origin": "KBP",
        "destination": "KBP",
        "price": -2500,
    },
    seat_number=201,
    has_baggage=True,
)

print(ticket.passenger.full_name)
print(ticket.flight.route)
print(ticket.total_price)
print(ticket1.passenger.full_name)
print(ticket1.flight.route)
print(ticket1.total_price)
