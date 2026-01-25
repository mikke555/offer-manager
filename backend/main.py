from contextlib import asynccontextmanager

from api.routes import master_router
from database.database import init_db
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from tests.utils import insert_dummy_data


def generate_unique_id(route: APIRoute) -> str:
    return route.name


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    insert_dummy_data()
    yield


description = """
### Get, create, update and delete offers.
### Manage custom payots for individual influencers.
"""


app = FastAPI(
    lifespan=lifespan,
    title="Offer Manager",
    description=description,
    generate_unique_id_function=generate_unique_id,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(master_router)
