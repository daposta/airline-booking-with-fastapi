import datetime
import uuid
from models.models import FlightBooking, FlightSchedule
from fastapi import HTTPException
from tables.tables import Airports, FlightSchedules


def add_airport_to_db(db, airport):
    db_airport = Airports(**airport.dict())
    db.add(db_airport)
    db.commit()
    db.refresh(db_airport)
    return airport


def fetch_airports_from_db(db):
    return db.query(Airports).all()


def read_airport_by_code(db, code):
    return db.query(Airports).filter_by(code=code).first()


def get_flights_from_db(db):
    return db.query(FlightSchedules).all()
