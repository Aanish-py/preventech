from fastapi import APIRouter
from .. import ml_model
router = APIRouter()
@router.post("/api/admin/retrain-model")
def retrain_model():
    return ml_model.train_model()