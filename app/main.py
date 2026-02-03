from fastapi import FastAPI, UploadFile, File
from app.preprocess import preprocess_image, segment_characters
from app.predict import predict_characters
from app.solver import solve_equation
from app.schemas import SolveResponse
import cv2
import numpy as np

app = FastAPI(title="Handwritten Equation Solver")

@app.post("/solve", response_model=SolveResponse)
async def solve(file: UploadFile = File(...)):
    contents = await file.read()
    np_img = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    processed = preprocess_image(image)
    chars = segment_characters(processed)
    equation = predict_characters(chars)
    solution = solve_equation(equation)

    return {
        "equation": equation,
        "solution": solution
    }
