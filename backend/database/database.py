from sqlmodel import SQLModel, create_engine

DB_URL = "sqlite:///local.db"

engine = create_engine(DB_URL)


def init_db():
    SQLModel.metadata.create_all(engine)
