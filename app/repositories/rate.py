from pydantic import BaseModel

from app.models.rate import Rate
from app.repositories.base import BaseRepository


class RateRepository(BaseRepository):
    model = Rate
