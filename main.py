from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.database import close_db, init_db
import uvicorn

from routes import user_router, file_router, auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # init stuff and give for request
    init_db()
    yield
    close_db()


app = FastAPI()
app.include_router(user_router)
app.include_router(file_router)
app.include_router(auth_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
