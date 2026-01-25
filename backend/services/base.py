from core.exceptions import NotFoundException
from fastapi import Response, status
from pydantic import BaseModel
from sqlmodel import Session, SQLModel, select


class BaseService:
    model: SQLModel = None
    schema: BaseModel = None
    name: str = None

    def __init__(self, session: Session):
        self.session = session

    def _get(self, id: int) -> SQLModel:
        db_item = self.session.get(self.model, id)
        if not db_item:
            raise NotFoundException(id=id, name=self.name)
        return db_item

    def get(self, id: int) -> BaseModel:
        db_item = self._get(id)
        return self.schema.model_validate(db_item)

    def _get_by(self, **filter_by) -> SQLModel:
        statement = select(self.model).filter_by(**filter_by)
        db_item = self.session.exec(statement).first()
        if not db_item:
            raise NotFoundException(id=id, name=self.name)
        return db_item

    def get_by(self, **filter_by) -> BaseModel:
        db_item = self._get_by(**filter_by)
        return self.schema.model_validate(db_item)

    def exists(self, **filter_by) -> bool:
        statement = select(self.model).filter_by(**filter_by)
        return self.session.exec(statement).first() is not None

    def list_by(self, *options, **filter_by) -> list[BaseModel]:
        statement = select(self.model).filter_by(**filter_by)
        if options:
            statement = statement.options(*options)
        db_items = self.session.exec(statement).all()
        return [self.schema.model_validate(item) for item in db_items]

    def delete(self, id: int) -> Response:
        db_item = self._get(id)
        self.session.delete(db_item)
        self.session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    def delete_by(self, **filter_by) -> Response:
        db_item = self._get_by(**filter_by)
        self.session.delete(db_item)
        self.session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
