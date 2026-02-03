import tensorflow as tf
from tensorflow.keras import layers, models

def create_model(num_classes=14):
    """
    Creates a simple CNN model for character recognition.
    Classes: 0-9, +, -, *, / (Total 14)
    """
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

if __name__ == "__main__":
    # If run directly, create and save a dummy model for initial testing
    model = create_model()
    model.save('../model/cnn_char_model.h5')
    print("Dummy model created and saved to ../model/cnn_char_model.h5")
