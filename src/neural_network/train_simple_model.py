import os
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import EarlyStopping, CSVLogger

BASE_DIR = "data/processed"
TRAIN_DIR = os.path.join(BASE_DIR, "train")
VAL_DIR = os.path.join(BASE_DIR, "validation")
MODEL_SAVE_PATH = "models/simple_model.h5"
RESULTS_DIR = "results"

# Parametrii Rețelei
IMG_SIZE = (64, 64)
BATCH_SIZE = 32
EPOCHS = 30 # Mai putine epoci pentru demo

def load_datasets():
    print("Încărcare date de antrenare (Simple Model)...")
    train_ds = tf.keras.utils.image_dataset_from_directory(
        TRAIN_DIR,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        label_mode='categorical'
    )
    val_ds = tf.keras.utils.image_dataset_from_directory(
        VAL_DIR,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        label_mode='categorical'
    )
    
    class_names = train_ds.class_names
    
    # Doar normalizare, fara augmentare complexa pentru acest model simplu
    norm_layer = layers.Rescaling(1./255)
    train_ds = train_ds.map(lambda x, y: (norm_layer(x), y))
    val_ds = val_ds.map(lambda x, y: (norm_layer(x), y))
    
    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=tf.data.AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=tf.data.AUTOTUNE)
    
    return train_ds, val_ds, class_names

def build_simple_cnn(num_classes):
    """Arhitectura Simpla (Shallow CNN) - pentru comparatie"""
    model = models.Sequential([
        # Doar 1 strat convolutional
        layers.Conv2D(16, (3, 3), activation='relu', input_shape=(64, 64, 3)),
        layers.MaxPooling2D((2, 2)),
        
        layers.Flatten(),
        layers.Dense(32, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

if __name__ == "__main__":
    train_ds, val_ds, class_names = load_datasets()
    model = build_simple_cnn(len(class_names))
    model.summary()
    
    callbacks = [
        EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True),
        CSVLogger(os.path.join(RESULTS_DIR, 'simple_model_history.csv'))
    ]

    print("\nÎncepe antrenarea modelului SIMPLU...")
    history = model.fit(train_ds, validation_data=val_ds, epochs=EPOCHS, callbacks=callbacks)
    
    # Salvare
    try:
        model.save(MODEL_SAVE_PATH)
    except:
        model.save(MODEL_SAVE_PATH.replace('.h5', '.keras'))
        
    # Afisare rezultat final
    val_acc = history.history['val_accuracy'][-1]
    print(f"\nSimple Model Validation Accuracy: {val_acc:.4f}")
