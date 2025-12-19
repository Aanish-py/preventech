from pydantic import BaseModel
from typing import Optional, Dict, Any

class RiskPredictionRequest(BaseModel):
    area_code: str
    disease: str = "dengue"
    temperature: Optional[float] = None
    rainfall: Optional[float] = None
    humidity: Optional[float] = None

class RiskPredictionResponse(BaseModel):
    risk_score: float
    risk_label: str
    disease: str
    explanatory_features: Dict[str, Any]

class StatSummary(BaseModel):
    total_cases: int
    high_risk_areas: int
    last_updated: str