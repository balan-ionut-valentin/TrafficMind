import os
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, CSVLogger

BASE_DIR = "data/processed"
TRAIN_DIR = os.path.join(BASE_DIR, "train")
VAL_DIR = os.path.join(BASE_DIR, "validation")
MODEL_SAVE_PATH = "models/trained_model.h5"
RESULTS_DIR = "results"
DOCS_DIR = "docs"

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs("models", exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs("models", exist_ok=True)

# Parametrii Rețelei
IMG_SIZE = (64, 64)
BATCH_SIZE = 32
EPOCHS = 50 


def get_data_augmentation():
    """Definire straturi de augmentare"""
    data_augmentation = tf.keras.Sequential([
        layers.RandomRotation(0.05),
        layers.RandomZoom(0.1),
        layers.RandomContrast(0.1),
        layers.RandomBrightness(0.1),
    ])
    return data_augmentation

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
    
    # Definire augmentare
    data_augmentation = get_data_augmentation()
    
    # Aplicare augmentare pe setul de antrenare
    # Folosim lambda pentru a aplica doar pe imagini (x), lăsând etichetele (y) neschimbate
    train_ds = train_ds.map(lambda x, y: (data_augmentation(x, training=True), y), 
                            num_parallel_calls=tf.data.AUTOTUNE)
    
    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=tf.data.AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=tf.data.AUTOTUNE)
    
    return train_ds, val_ds, class_names

def build_cnn_model(num_classes):
    """Construiește arhitectura CNN."""
    model = models.Sequential([
        # Strat de normalizare (Augmentarea e acum in dataset)
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
    
    # Salvare grafic cerut
    loss_curve_path = os.path.join(DOCS_DIR, 'loss_curve.png')
    plt.savefig(loss_curve_path)
    print(f"Graficele au fost salvate ca '{loss_curve_path}'")
    plt.close()

if __name__ == "__main__":
    train_ds, val_ds, class_names = load_datasets()
    
    num_classes = len(class_names)
    print(f"Clase identificate ({num_classes}): {class_names}")
    
    model = build_cnn_model(num_classes)
    model.summary()
    
    # Definire callback-uri
    callbacks = [
        EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True, verbose=1),
        ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3, min_lr=0.00001, verbose=1),
        CSVLogger(os.path.join(RESULTS_DIR, 'training_history.csv'))
    ]

    print("\nÎncepe antrenarea modelului...")
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=EPOCHS,
        callbacks=callbacks
    )
    
    # Stergem fisierul vechi daca exista pentru a evita conflicte de permisiuni rare
    if os.path.exists(MODEL_SAVE_PATH):
        try:
            os.remove(MODEL_SAVE_PATH)
        except:
            pass
            
    try:
        model.save(MODEL_SAVE_PATH)
        print(f"\nModel salvat cu succes în '{MODEL_SAVE_PATH}'")
    except Exception as e:
        print(f"\nEROARE la salvarea .h5: {e}")
        print("Incercare salvare in format .keras (formatul modern)...")
        NEW_PATH = MODEL_SAVE_PATH.replace('.h5', '.keras')
        model.save(NEW_PATH)
        print(f"Model salvat în '{NEW_PATH}'. Actualizeaza scripturile de inferenta!")
    
    plot_history(history)