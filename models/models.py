from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from datetime import datetime


class Airport(BaseModel):
    name: str = Field(
        min_length=3,
    )
    code: str = Field(
        min_length=3,
    )
    country: str = Field(min_length=3)


class FlightSchedule(BaseModel):
    departure: Airport
    arrival: Airport
    departure_datetime: datetime
    arrival_datetime: datetime
    price: float
    available_seats: int


class Person(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: str
    email: str
    phone_number: str


class BookingStatus(str, Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"


class FlightBooking(BaseModel):
    flight: FlightSchedule
    location: Airport
    quantity: int
    total_price: float
    person: Person
    status: BookingStatus = Field(
        BookingStatus.PENDING, description="Status of the item"
    )  # BookingStatusEnum.PENDING
    booking_timestamp: datetime


class FlightStatusStatus(str, Enum):
    PENDING = "On time"
    CONFIRMED = "Delayed"
    CANCELLED = "Canceled"


# class FlightStatus(BaseModel):
#     id: uuid = uuid.uuid4()
#     flight: FlightSchedule
#     status: FlightStatusStatus


class FlightHistory(BaseModel):
    flight: FlightSchedule
    location: Airport
    quantity: int
    total_price: float
    person: Person
    status: FlightStatusStatus
