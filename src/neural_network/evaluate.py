import os
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix, f1_score, accuracy_score

BASE_DIR = "../../data/processed"
TEST_DIR = os.path.join(BASE_DIR, "test")
MODEL_PATH = "../../models/trained_model.h5"
RESULTS_DIR = "../../results"
DOCS_DIR = "../../docs"
IMG_SIZE = (64, 64)
BATCH_SIZE = 32

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)

def load_test_data():
    print("Încărcare date de test...")
    test_ds = tf.keras.utils.image_dataset_from_directory(
        TEST_DIR,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        label_mode='categorical',
        shuffle=False
    )
    return test_ds, test_ds.class_names

def evaluate_model():
    if not os.path.exists(MODEL_PATH):
        print(f"Eroare: Fișierul {MODEL_PATH} nu există! Rulați întâi train_model.py.")
        return

    print(f"Încărcare model din {MODEL_PATH}...")
    model = tf.keras.models.load_model(MODEL_PATH)
    
    test_ds, class_names = load_test_data()
    
    print("\nGenerare predicții...")
    y_true = []
    y_pred = []
    
    for images, labels in test_ds:
        preds = model.predict(images, verbose=0)
        y_true.extend(np.argmax(labels.numpy(), axis=1))
        y_pred.extend(np.argmax(preds, axis=1))
        
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    # Calcul Metrici
    acc = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred, average='macro')
    
    print(f"\n--- Rezultate Evaluare ---")
    print(f"Test Accuracy: {acc:.4f}")
    print(f"Test F1-Score (Macro): {f1:.4f}")
    
    # Salvare metrici JSON
    metrics = {
        "test_accuracy": float(acc),
        "test_f1_macro": float(f1),
        "classes": class_names
    }
    
    metrics_path = os.path.join(RESULTS_DIR, "test_metrics.json")
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=4)
    print(f"Metrici salvate în {metrics_path}")
    
    # Confusion Matrix
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title('Confusion Matrix')
    
    cm_path = os.path.join(DOCS_DIR, "confusion_matrix.png")
    plt.savefig(cm_path)
    print(f"Matricea de confuzie salvată în {cm_path}")
    plt.close()
    
    # Raport detaliat
    print("\n--- Raport Detaliat ---")
    print(classification_report(y_true, y_pred, target_names=class_names))

if __name__ == "__main__":
    evaluate_model()
