import os
# Suppress oneDNN logs
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import argparse
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, CSVLogger

# Default Paths
BASE_DIR = "data/processed"
TRAIN_DIR = os.path.join(BASE_DIR, "train")
VAL_DIR = os.path.join(BASE_DIR, "validation")
RESULTS_DIR = "results"
DOCS_DIR = "docs"
MODELS_DIR = "models"

# Ensure directories exist
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)

# Default Parameters
IMG_SIZE = (64, 64)

def get_data_augmentation():
    """Definire straturi de augmentare"""
    data_augmentation = tf.keras.Sequential([
        layers.RandomRotation(0.05),
        layers.RandomZoom(0.1),
        layers.RandomContrast(0.1),
        layers.RandomBrightness(0.1),
    ])
    return data_augmentation

def load_datasets(batch_size):
    """Încarcă datele direct din foldere folosind Keras."""
    print(f"Încărcare date (Batch Size: {batch_size})...")
    
    train_ds = tf.keras.utils.image_dataset_from_directory(
        TRAIN_DIR,
        image_size=IMG_SIZE,
        batch_size=batch_size,
        label_mode='categorical'
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        VAL_DIR,
        image_size=IMG_SIZE,
        batch_size=batch_size,
        label_mode='categorical'
    )
    
    class_names = train_ds.class_names
    
    # Definire augmentare
    data_augmentation = get_data_augmentation()
    
    # Aplicare augmentare pe setul de antrenare
    train_ds = train_ds.map(lambda x, y: (data_augmentation(x, training=True), y), 
                            num_parallel_calls=tf.data.AUTOTUNE)
    
    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=tf.data.AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=tf.data.AUTOTUNE)
    
    return train_ds, val_ds, class_names

def build_cnn_model(num_classes, learning_rate=0.001, dropout_rate=0.5, dense_units=64):
    """Construiește arhitectura CNN cu parametri variabili."""
    model = models.Sequential([
        # Strat de normalizare
        layers.Rescaling(1./255, input_shape=(IMG_SIZE[0], IMG_SIZE[1], 3)),
        
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
        layers.Dense(dense_units, activation='relu'),
        layers.Dropout(dropout_rate),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    optimizer = optimizers.Adam(learning_rate=learning_rate)
    
    model.compile(optimizer=optimizer,
                  loss='categorical_crossentropy',
                  metrics=['accuracy', tf.keras.metrics.F1Score(average='macro', name='f1_score')])
    
    return model

def plot_history(history, experiment_name):
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
    plt.title(f'Accuracy - {experiment_name}')

    # Grafic Eroare
    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title(f'Loss - {experiment_name}')
    
    # Salvare grafic
    # Folosim experiment_name în filename pentru a nu suprascrie
    filename = f'loss_curve_{experiment_name}.png'
    save_path = os.path.join(DOCS_DIR, filename)
    plt.savefig(save_path)
    print(f"Graficele au fost salvate ca '{save_path}'")
    plt.close()

def train(batch_size, epochs, learning_rate, dropout, dense_units, experiment_name, early_stopping=False):
    print(f"--- Starting Experiment: {experiment_name} ---")
    print(f"Params: Batch={batch_size}, Epochs={epochs}, LR={learning_rate}, Dropout={dropout}, Dense={dense_units}, EarlyStopping={early_stopping}")

    # 1. Load Data
    train_ds, val_ds, class_names = load_datasets(batch_size)
    num_classes = len(class_names)
    print(f"Clase: {class_names}")
    
    # 2. Build Model
    model = build_cnn_model(num_classes, learning_rate, dropout, dense_units)
    # model.summary() # Optional, too verbose for batch runs
    
    # 3. Callbacks
    # Save generic history content appended
    history_file = os.path.join(RESULTS_DIR, f'history_{experiment_name}.csv')
    
    callbacks = [
        ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3, min_lr=0.00001, verbose=1),
        CSVLogger(history_file)
    ]
    
    if early_stopping:
        callbacks.append(EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True, verbose=1))

    # 4. Train
    print("Începe antrenarea...")
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs,
        callbacks=callbacks,
        verbose=1 
    )
    
    # 5. Save Model
    # Nume model specific experimentului, sau generic daca e "optimized"
    model_filename = f"{experiment_name}_model.h5"
    model_path = os.path.join(MODELS_DIR, model_filename)
        
    try:
        model.save(model_path)
        print(f"Model salvat: {model_path}")
    except Exception as e:
        print(f"Eroare salvare .h5: {e}. Trying .keras")
        model.save(model_path.replace('.h5', '.keras'))
    
    # 6. Plot
    plot_history(history, experiment_name)
    
    # Return final metrics
    final_acc = history.history['val_accuracy'][-1]
    final_loss = history.history['val_loss'][-1]
    print(f"Experiment {experiment_name} finished. Val Acc: {final_acc:.4f}")
    return final_acc, final_loss

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Antrenare Retea Neuronala TrafficMind")
    parser.add_argument('--batch', '--batch_size', dest='batch', type=int, default=32, help='Batch size')
    parser.add_argument('--epochs', type=int, default=50, help='Numar epoci')
    parser.add_argument('--lr', type=float, default=0.001, help='Learning Rate')
    parser.add_argument('--dropout', type=float, default=0.5, help='Dropout rate')
    parser.add_argument('--dense', type=int, default=64, help='Numar neuroni in stratul dens')
    parser.add_argument('--name', type=str, default='trained', help='Nume experiment (pentru fisiere output)')
    parser.add_argument('--early_stopping', action='store_true', help='Activeaza Early Stopping')
    
    args = parser.parse_args()
    
    train(args.batch, args.epochs, args.lr, args.dropout, args.dense, args.name, args.early_stopping)