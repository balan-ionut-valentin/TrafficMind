import os
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models

BASE_DIR = "../../data/processed"
TRAIN_DIR = os.path.join(BASE_DIR, "train")
VAL_DIR = os.path.join(BASE_DIR, "validation")
MODEL_SAVE_PATH = "traffic_sign_model.h5"

# Parametrii Rețelei
IMG_SIZE = (64, 64)
BATCH_SIZE = 32
EPOCHS = 15

def load_datasets():
    """Încarcă datele direct din foldere folosind Keras."""
    print("Încărcare date de antrenare...")
    train_ds = tf.keras.utils.image_dataset_from_directory(
        TRAIN_DIR,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        label_mode='categorical'
    )

    print("Încărcare date de validare...")
    val_ds = tf.keras.utils.image_dataset_from_directory(
        VAL_DIR,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        label_mode='categorical'
    )
    
    class_names = train_ds.class_names
    
    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=tf.data.AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=tf.data.AUTOTUNE)
    
    return train_ds, val_ds, class_names

def build_cnn_model(num_classes):
    """Construiește arhitectura CNN."""
    model = models.Sequential([
        # Strat de normalizare 
        layers.Rescaling(1./255, input_shape=(64, 64, 3)),
        
        # Bloc 1 Convoluțional
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        # Bloc 2 Convoluțional
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        # Bloc 3 Convoluțional
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        # "Aplatizare" și strat dens
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
    return model

def plot_history(history):
    """Generează graficele de antrenare."""
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    
    epochs_range = range(len(acc))

    plt.figure(figsize=(12, 4))
    
    # Grafic Acuratețe
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Acuratețe (Accuracy)')

    # Grafic Eroare
    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Eroare (Loss)')
    
    plt.savefig('training_plot.png')
    print("Graficele au fost salvate ca 'training_plot.png'")

if __name__ == "__main__":
    train_ds, val_ds, class_names = load_datasets()
    
    num_classes = len(class_names)
    print(f"Clase identificate ({num_classes}): {class_names}")
    
    model = build_cnn_model(num_classes)
    model.summary()
    
    print("\nÎncepe antrenarea modelului...")
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=EPOCHS
    )
    
    model.save(MODEL_SAVE_PATH)
    print(f"\nModel salvat cu succes în '{MODEL_SAVE_PATH}'")
    
    plot_history(history)