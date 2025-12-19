from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, models, database, ml_model
from datetime import date

router = APIRouter()

@router.post("/api/predict", response_model=schemas.RiskPredictionResponse)
def get_prediction(req: schemas.RiskPredictionRequest, db: Session = Depends(database.get_db)):
    env_record = db.query(models.EnvironmentRecord).filter(
        models.EnvironmentRecord.area_code == req.area_code,
        models.EnvironmentRecord.date == date.today()
    ).first()

    temp = env_record.temperature if env_record else (req.temperature or 28.0)
    rain = env_record.rainfall if env_record else (req.rainfall or 0.0)
    hum = env_record.humidity if env_record else (req.humidity or 60.0)
    pop = env_record.population_density if env_record else 1000.0

    prob = ml_model.predict_risk(temp, rain, hum, pop)
    label = "High" if prob > 0.7 else "Moderate" if prob > 0.4 else "Low"

    return {
        "risk_score": round(prob, 2),
        "risk_label": label,
        "disease": req.disease,
        "explanatory_features": {"temperature": temp, "rainfall": rain, "humidity": hum}
    }