from datetime import datetime
from pydantic import BaseModel


class PredictionRequest(BaseModel):
    timestamp: datetime