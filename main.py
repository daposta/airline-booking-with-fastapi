from fastapi import FastAPI
from config.db import Base, engine
from routes.public import routes as public

app = FastAPI()

# create db tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def index():
    return {"message": "Hello passengers, this is your pilot!"}


app.include_router(public.router)
