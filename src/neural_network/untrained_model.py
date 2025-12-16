import os
import tensorflow as tf
from tensorflow.keras import layers, models

MODEL_SAVE_PATH = "../../models/untrained_model.h5"

def build_cnn_model(num_classes=8):
    model = models.Sequential([
        layers.Rescaling(1./255, input_shape=(64, 64, 3)),
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

if __name__ == "__main__":
    os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)
    
    model = build_cnn_model()
    
    model.save(MODEL_SAVE_PATH)
    print(f"Model NEANTRAT salvat în: {MODEL_SAVE_PATH}")
