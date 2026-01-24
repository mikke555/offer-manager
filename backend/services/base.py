from fastapi import Response, status
from pydantic import BaseModel
from sqlmodel import Session, select

from core.exceptions import NotFoundException


class BaseService:
    model = None
    schema: BaseModel = None

    def __init__(self, session: Session):
        self.session = session

    def _get(self, id: int):
        db_item = self.session.get(self.model, id)
        if not db_item:
            raise NotFoundException
        return db_item

    def get(self, id: int) -> BaseModel:
        db_item = self._get(id)
        return self.schema.model_validate(db_item)

    def get_by(self, **filter_by):
        statement = select(self.model).filter_by(**filter_by)
        db_item = self.session.exec(statement).first()
        if not db_item:
            raise NotFoundException
        return db_item

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
        db_item = self.get_by(**filter_by)
        self.session.delete(db_item)
        self.session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
