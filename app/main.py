from fastapi import FastAPI
from database.db import create_tables
from routers.routers import router
import uvicorn

app = FastAPI()

app.include_router(router, prefix="/user")

create_tables()

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True)
