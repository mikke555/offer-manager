from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.routes import master_router
from database.database import init_db
from tests.utils import insert_dummy_data


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    insert_dummy_data()
    yield


description = """
### Get, create, update and delete offers.
### Manage custom payots for individual influencers.
"""


app = FastAPI(lifespan=lifespan, title="Offer Manager", description=description)
app.include_router(master_router)
