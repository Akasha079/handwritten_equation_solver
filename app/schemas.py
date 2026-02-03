from pydantic import BaseModel

class PredictionRequest(BaseModel):
    image: str  # Base64 encoded image

class PredictionResponse(BaseModel):
    equation: str
    solution: str
    confidence: float
