from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app import models, schemas

router = APIRouter()

@router.post("/form/createData", response_model=schemas.FormOut)
async def create_form(data: schemas.FormCreate, db: AsyncSession = Depends(get_db)):
    new_entry = models.FormData(**data.dict())
    db.add(new_entry)
    await db.commit()
    await db.refresh(new_entry)
    return new_entry

@router.get("/form/getallData", response_model=list[schemas.FormOut])
async def get_all_form_data(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.FormData))
    return result.scalars().all()
