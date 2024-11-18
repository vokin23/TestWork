from fastapi import APIRouter, HTTPException

from app.routers.dependencies import DBDep
from app.schemas.rate import RateCreate, Rate, CalculateInsuranceSchema

router = APIRouter(prefix="/rate")


@router.post("/", summary='Метод для создания Rate')
async def create(db: DBDep, data: RateCreate) -> Rate:
    return await db.rate.create(data)

@router.get("/", summary='Метод для получения всех Rate')
async def get_all(db: DBDep):
    return await db.rate.all()

@router.get("/calculate_insurance", summary='Метод для расчета страховки')
async def calculate_insurance(db: DBDep, cargo_type: str, declared_value: float, date: str):
    rate = await db.rate.get(cargo_type=cargo_type, date=date)
    if not rate:
        raise HTTPException(status_code=404, detail="Rate not found")
    return {"insurance": rate.rate * declared_value}
