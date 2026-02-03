from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from .schemas import PredictionRequest, PredictionResponse
from .predict import predict_equation, load_prediction_model
import os

app = FastAPI(title="Handwritten Equation Solver")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

@app.on_event("startup")
async def startup_event():
    load_prediction_model()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    result = predict_equation(request.image)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
