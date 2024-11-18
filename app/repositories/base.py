from datetime import datetime

from sqlalchemy import select, insert
from pydantic import BaseModel


class BaseRepository:
    model = None
    schema = None

    def __init__(self, session):
        self.session = session

    async def all(self):
        obj_stmt = select(self.model)
        result = await self.session.execute(obj_stmt)
        return result.scalars().all()

    async def create(self, data: BaseModel):
        obj_stmt = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(obj_stmt)
        await self.session.commit()
        return result.scalar()

    async def get(self, **filter_by):
        if 'date' in filter_by:
            filter_by['date'] = datetime.strptime(filter_by['date'], '%Y-%m-%d').date()
        obj_stmt = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(obj_stmt)
        return result.scalar()
