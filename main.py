from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.database import init_db
from routes.fileRoutes import router as fileRoutes
from routes.userRoutes import router as userRoutes


@asynccontextmanager
async def lifespan(app: FastAPI):
    # init stuff and give for request
    init_db()
    yield


app = FastAPI()
app.include_router(userRoutes)
app.include_router(fileRoutes)


@app.get("/")
def read_root():
    return {"Hello": "World"}
