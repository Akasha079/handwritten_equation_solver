import cv2
import numpy as np
import base64

def base64_to_image(base64_string: str) -> np.ndarray:
    """Converts base64 string to OpenCV image."""
    if ',' in base64_string:
        base64_string = base64_string.split(',')[1]
    img_data = base64.b64decode(base64_string)
    nparr = np.frombuffer(img_data, np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

def preprocess_image(image: np.ndarray):
    """
    detects characters in the image and processes them for the model.
    Returns a list of (rect, char_img_processed) tuples, sorted from left to right.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Thresholding (inverted because canvas is usually white background with black text, 
    # but we trained on EMNIST/MNIST which is white text on black background so we want that usually,
    # let's assume valid strokes are dark on light for user input, so we use THRESH_BINARY_INV)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    char_list = []
    
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        
        # Filter small noise
        if w < 10 or h < 10:
            continue
            
        roi = thresh[y:y+h, x:x+w]
        
        # Add padding to make it square and center the character
        # Model expects 28x28 usually
        max_dim = max(w, h)
        pad_size = int(max_dim * 1.2)
        padded_roi = np.zeros((pad_size, pad_size), dtype=np.uint8)
        
        center_x = pad_size // 2
        center_y = pad_size // 2
        
        start_x = center_x - w // 2
        start_y = center_y - h // 2
        
        padded_roi[start_y:start_y+h, start_x:start_x+w] = roi
        
        # Resize to 28x28
        resized = cv2.resize(padded_roi, (28, 28), interpolation=cv2.INTER_AREA)
        
        # Normalize
        normalized = resized.astype('float32') / 255.0
        normalized = np.expand_dims(normalized, axis=-1) # (28, 28, 1)
        
        char_list.append(((x, y, w, h), normalized))
        
    # Sort by X coordinate (left to right)
    char_list.sort(key=lambda item: item[0][0])
    
    return [c[1] for c in char_list]
