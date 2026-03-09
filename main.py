from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # init stuff and give for request
    yield


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
