import numpy as np
import tensorflow as tf
from .preprocess import base64_to_image, preprocess_image
from .solver import solve_equation

# Mapping indices to characters
# 0-9 are 0-9
# 10: +, 11: -, 12: *, 13: /
CLASS_MAPPING = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: '+', 11: '-', 12: '*', 13: '/'
}

model = None

def load_prediction_model(path: str = '../model/cnn_char_model.h5'):
    global model
    try:
        model = tf.keras.models.load_model(path)
        print("Model loaded successfully")
    except Exception as e:
        print(f"Failed to load model: {e}")
        model = None

def predict_equation(base64_image: str):
    """
    Main pipeline:
    1. Decode image
    2. Preprocess (segmentation)
    3. Predict characters
    4. Form equation string
    5. Solve
    """
    if model is None:
        load_prediction_model()
        if model is None:
            return {"equation": "", "solution": "Error: Model not loaded", "confidence": 0.0}

    image = base64_to_image(base64_image)
    chars = preprocess_image(image)
    
    if not chars:
        return {"equation": "", "solution": "No equation detected", "confidence": 0.0}
    
    # Batch predict
    batch_chars = np.array(chars) # (N, 28, 28, 1)
    predictions = model.predict(batch_chars)
    
    equation_components = []
    confidences = []
    
    for pred in predictions:
        class_idx = np.argmax(pred)
        conf = np.max(pred)
        equation_components.append(CLASS_MAPPING.get(class_idx, '?'))
        confidences.append(conf)
        
    equation_str = "".join(equation_components)
    solution = solve_equation(equation_str)
    avg_confidence = float(np.mean(confidences))
    
    return {
        "equation": equation_str,
        "solution": solution,
        "confidence": avg_confidence
    }
