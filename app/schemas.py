from pydantic import BaseModel

class SolveResponse(BaseModel):
    equation: str
    solution: str
