from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes import lci
from app.db.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="LCI Database", lifespan=lifespan)

app.include_router(lci.router, prefix="/api/lci", tags=["LCI"])
