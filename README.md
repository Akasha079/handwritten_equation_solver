✍️ Handwritten Equation Solver

An AI-powered system to solve handwritten mathematical equations.
The system uses Convolutional Neural Networks (CNN) for character recognition, OpenCV for image preprocessing, and SymPy for multi-step equation solving. Everything is exposed through a FastAPI REST API for easy integration.

🚀 Features

📷 Upload handwritten equations as images

🤖 CNN-based OCR to recognize digits and operators

✍️ Supports 0-9, +, -, *, /, (, )

🧮 Multi-step equation solving using SymPy

⚡ FastAPI-based REST API for quick deployment

🔁 Modular code for easy training and upgrades

🧠 Tech Stack

Backend: FastAPI

Computer Vision: OpenCV

Deep Learning: TensorFlow/Keras (CNN)

Math Solver: SymPy

Language: Python

Deployment-ready: Docker-friendly structure

📁 Project Structure
handwritten_equation_solver/
│
├── app/
│   ├── main.py            # FastAPI app
│   ├── preprocess.py      # Image preprocessing & character segmentation
│   ├── cnn_model.py       # CNN architecture
│   ├── predict.py         # Character prediction
│   ├── solver.py          # Equation solving
│   └── schemas.py         # Pydantic response models
│
├── model/
│   └── cnn_char_model.h5  # Pre-trained CNN model
│
├── requirements.txt
└── README.md

⚙️ Installation

Clone the repository

git clone https://github.com/AkashaMeh/handwritten-equation-solver.git
cd handwritten-equation-solver


Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt

▶️ Running the Application
uvicorn app.main:app --reload


Open Swagger UI for testing:

http://127.0.0.1:8000/docs

📌 API Endpoints
🔹 Solve Handwritten Equation

POST /solve

Request:

Form-data upload of image file

Response:

{
  "equation": "12+7*3",
  "solution": "33"
}

🔁 How it Works

Image Preprocessing: Converts uploaded image to grayscale, thresholds, and dilates for better segmentation.

Character Segmentation: Detects individual characters from the equation.

CNN Recognition: Each character is predicted using a trained CNN model.

Equation Reconstruction: Converts predicted characters into a full math expression.

Equation Solving: SymPy evaluates the expression and returns the result.

🧪 Example

Upload an image containing:

(5+3)*2


API Response:

{
  "equation": "(5+3)*2",
  "solution": "16"
}

💼 Future Improvements

Train CNN on larger datasets like EMNIST with symbols

Replace segmentation with CRNN for end-to-end recognition

Add LaTeX output

Deploy on Raspberry Pi / Edge devices

Dockerize for production deployment

👩‍💻 Author

Akasha Mehmood
📎 GitHub: github.com/AkashaMeh

📎 LinkedIn: linkedin.com/in/akasha-mehmood