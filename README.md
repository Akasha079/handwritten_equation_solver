# ✍️ HandySolve AI: Professional Handwritten Equation Solver

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68%2B-009688)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

<div align="center">
  <h3>✨ Turn your handwritten scrawls into solved math instantly. ✨</h3>
  <p>An advanced, AI-powered web application capable of recognizing and solving handwritten mathematical equations in real-time. Features a stunning Glassmorphism UI and a robust microservices-ready backend.</p>
</div>

---

## 🚀 Overview

**HandySolve AI** bridges the gap between traditional handwriting and digital computation. Users can draw equations on an interactive canvas, and the system uses a Convolutional Neural Network (CNN) to recognize character-by-character, reconstruct the equation, and compute the result via a symbolic solver.

### Key Features
- **🎨 Interactive Canvas**: Smooth, responsive drawing experience on both desktop and touch devices.
- **✨ Glassmorphism UI**: A visually premium interface with modern animations and aesthetic gradients.
- **🧠 AI-Powered OCR**: Custom CNN implementation to detect digits and operators (`0-9`, `+`, `-`, `*`, `/`).
- **⚡ Real-time Solving**: Instant feedback with confidence scoring.
- **🔌 REST API**: Full-featured FastAPI backend exposing prediction endpoints.

## 🛠️ Tech Stack

### Frontend
- **HTML5 Canvas**: For high-performance drawing interpretation.
- **Vanilla CSS3**: Custom responsive design with Glassmorphism effects (No frameworks used, pure CSS).
- **JavaScript (ES6+)**: Async/Await API integration and touch event handling.

### Backend
- **FastAPI**: High-performance, async web framework.
- **OpenCV**: Image preprocessing (contour detection, noise reduction).
- **TensorFlow/Keras**: Deep Learning model for character recognition.
- **NumPy**: Matrix operations and image transformations.

## 📂 Project Structure

```text
handwritten_equation_solver/
│
├── app/
│   ├── main.py              # 🚀 Application Entry Point
│   ├── cnn_model.py         # 🧠 CNN Architecture Definition
│   ├── preprocess.py        # 🖼️ Image Segmentation & Processing
│   ├── predict.py           # 🔮 Inference Pipeline
│   ├── solver.py            # 🧮 Mathematical Evaluation Logic
│   ├── schemas.py           # 📋 Pydantic Models for API
│   │
│   ├── templates/
│   │   └── index.html       # 🌐 Main Web Interface
│   └── static/
│       ├── style.css        # 🎨 App Styling
│       └── script.js        # 📜 Frontend Logic
│
├── model/
│   └── cnn_char_model.h5    # 🤖 Saved Model Weights
│
├── requirements.txt         # 📦 Dependencies
└── README.md                # 📄 Documentation
```

## ⚙️ Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/handwritten-equation-solver.git
cd handwritten-equation-solver
```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed.
```bash
pip install -r requirements.txt
```

### 3. Generate Model (First Run Only)
Since the model binary is large, we generate a fresh instance (or you can place your trained `.h5` file in `model/`).
```bash
python app/cnn_model.py
```

### 4. Run the Server
Start the development server:
```bash
uvicorn app.main:app --reload
```

### 5. Open the Application
Visit **[http://localhost:8000](http://localhost:8000)** in your browser.

## 🧪 API Documentation

The backend automatically generates interactive documentation.
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Endpoint: `/predict`
- **Method**: `POST`
- **Body**: JSON `{ "image": "base64_string..." }`
- **Response**:
  ```json
  {
    "equation": "2+2",
    "solution": "4",
    "confidence": 0.98
  }
  ```

## 🤝 Contributing

Contributions are welcome!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---
<div align="center">
  <p>Made with ❤️ by Jawwad</p>
</div>