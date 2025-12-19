from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import database, models, schemas
import datetime

router = APIRouter()

@router.get("/api/stats/summary", response_model=schemas.StatSummary)
def get_summary(db: Session = Depends(database.get_db)):
    total = db.query(func.sum(models.HospitalCase.cases)).scalar() or 0
    return {"total_cases": total, "high_risk_areas": 2, "last_updated": datetime.datetime.now().strftime("%H:%M:%S")}

@router.get("/api/stats/trends")
def get_trends(disease: str, area_code: str, db: Session = Depends(database.get_db)):
    records = db.query(models.HospitalCase).filter(
        models.HospitalCase.disease == disease, models.HospitalCase.area_code == area_code
    ).order_by(models.HospitalCase.date).all()
    return [{"date": r.date.strftime("%Y-%m-%d"), "cases": r.cases} for r in records]

@router.get("/api/stats/heatmap")
def get_heatmap():
    return [
        {"area_code": "AREA001", "lat": 18.5204, "lng": 73.8567, "risk_score": 0.8},
        {"area_code": "AREA002", "lat": 19.0760, "lng": 72.8777, "risk_score": 0.3}
    ]