from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello passengers, this is your pilot!"}
