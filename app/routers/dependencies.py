from typing import Annotated

from fastapi import Depends, Query, HTTPException, Request
from pydantic import BaseModel

from app.database import async_session_maker, async_session_maker_null_pool
from app.utils.db_manager import DBManager


class PaginationParams(BaseModel):
    page: Annotated[int | None, Query(1, ge=1)]
    per_page: Annotated[int | None, Query(None, ge=1, lt=30)]


PaginationDep = Annotated[PaginationParams, Depends()]


def get_db_manager():
    return


async def get_db():
    async with DBManager(session_factory=async_session_maker) as db:
        yield db

async def get_db_null_pull():
    async with DBManager(session_factory=async_session_maker_null_pool) as db:
        yield db


DBDep = Annotated[DBManager, Depends(get_db)]
DBDep_null_pull = Annotated[DBManager, Depends(get_db_null_pull, use_cache=False)]
