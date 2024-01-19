from fastapi import APIRouter
from controllers.public.controllers import (
    add_airport_to_db,
    fetch_airports_from_db,
    get_flights_from_db,
    read_airport_by_code,
)
from models.models import Airport
from utils import db_dependency

router = APIRouter()


@router.get("/airports")
def fetch_airports(db: db_dependency):
    return fetch_airports_from_db(db)


@router.post("/airports")
def add_airport(airport: Airport, db: db_dependency):
    return add_airport_to_db(db, airport)


@router.post("/airports/{code}")
def add_airport(code: str, db: db_dependency):
    return read_airport_by_code(db, code)


@router.get("/flights")
def get_flights(db: db_dependency):
    return get_flights_from_db(db)
