from sqlalchemy import Column, ForeignKey, Integer, String
import uuid
from sqlalchemy.dialects.mysql import CHAR
from config.db import Base


class Airports(Base):
    __tablename__ = "airports"

    id = Column(
        CHAR(36),
        primary_key=True,
        default=str(uuid.uuid4()),
        unique=True,
        nullable=False,
    )
    name = Column(String(50))
    code = Column(String(50))
    country = Column(String(50))


class FlightSchedules(Base):
    __tablename__ = "flight_schedules"

    id = Column(
        CHAR(36),
        primary_key=True,
        default=str(uuid.uuid4()),
        unique=True,
        nullable=False,
    )
    departure = Column(CHAR(36), ForeignKey("airports.id"))
    arrival = Column(CHAR(36), ForeignKey("airports.id"))
    departure_datetime = Column(String(50))
    arrival_datetime = Column(String(50))
    flight_status = Column(String(50))


class Persons(Base):
    __tablename__ = "persons"
    id = Column(
        CHAR(36),
        primary_key=True,
        default=str(uuid.uuid4()),
        unique=True,
        nullable=False,
    )
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50))
    phone_number = Column(String(50))


class FlightBookings(Base):
    __tablename__ = "flight_bookings"
    id = Column(
        CHAR(36),
        primary_key=True,
        default=str(uuid.uuid4()),
        unique=True,
        nullable=False,
    )
    flight = Column(CHAR(36), ForeignKey("flight_schedules.id"))
    passenger = Column(CHAR(36), ForeignKey("persons.id"))
    seat_number = Column(Integer)
