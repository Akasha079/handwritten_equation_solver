import numpy as np
from tensorflow.keras.models import load_model

MODEL_PATH = "model/cnn_char_model.h5"
model = load_model(MODEL_PATH)

LABELS = ['0','1','2','3','4','5','6','7','8','9',
          '+','-','*','/','(',')']

def predict_characters(chars):
    equation = ""
    for char in chars:
        char = char / 255.0
        char = char.reshape(1,28,28,1)
        pred = model.predict(char, verbose=0)
        equation += LABELS[np.argmax(pred)]
    return equation
