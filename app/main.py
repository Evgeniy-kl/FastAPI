from fastapi import FastAPI
from database.db import create_tables
from routers.api import router
import uvicorn

app = FastAPI()

app.include_router(router, prefix="/user")


@app.on_event("startup")
async def startup_event():
    create_tables()


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True)
