from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/b_user/')
async def get_b_user(db: Session = Depends(get_db)):
    return await service.get_b_user(db)

@router.get('/b_user/id')
async def get_b_user_id( id: int , db: Session = Depends(get_db)):
    return await service.get_b_user_id(db , id)

@router.post('/b_user/')
async def post_b_user( id: int, created_at: str , db: Session = Depends(get_db)):
    return await service.post_b_user(db , id, created_at)

@router.put('/b_user/id/')
async def put_b_user_id( id: str, created_at: str , db: Session = Depends(get_db)):
    return await service.put_b_user_id(db , id, created_at)

@router.delete('/b_user/id')
async def delete_b_user_id( id: int , db: Session = Depends(get_db)):
    return await service.delete_b_user_id(db , id)

