import os
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix, f1_score, accuracy_score

BASE_DIR = "data/processed"
TEST_DIR = os.path.join(BASE_DIR, "test")
MODEL_PATH = "models/trained_model.h5"
RESULTS_DIR = "results"
DOCS_DIR = "docs"
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

import argparse

def evaluate_model(model_path, output_json, output_cm):
    if not os.path.exists(model_path):
        print(f"Eroare: Fișierul {model_path} nu există!")
        return

    print(f"Încărcare model din {model_path}...")
    model = tf.keras.models.load_model(model_path)
    
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
    import time
    start_time = time.time()
    # Dummy predict to measure latency on single item (average of 100 runs)
    if len(test_ds) > 0:
        sample_img = next(iter(test_ds))[0][:1]
        for _ in range(50):
            model.predict(sample_img, verbose=0)
        t0 = time.time()
        for _ in range(100):
            model.predict(sample_img, verbose=0)
        dt = time.time() - t0
        latency_ms = (dt / 100) * 1000
    else:
        latency_ms = 0

    from sklearn.metrics import precision_score, recall_score
    
    acc = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred, average='macro')
    precision = precision_score(y_true, y_pred, average='macro')
    recall = recall_score(y_true, y_pred, average='macro')
    
    # Confusion Matrix for global FNR/FPR (Macro average approximation)
    cm = confusion_matrix(y_true, y_pred)
    FP = cm.sum(axis=0) - np.diag(cm)  
    FN = cm.sum(axis=1) - np.diag(cm)
    TP = np.diag(cm)
    TN = cm.sum() - (FP + FN + TP)

    # Macro average FNR/FPR
    FNR = np.mean(FN / (TP + FN + 1e-7))
    FPR = np.mean(FP / (TN + FP + 1e-7))

    print(f"\n--- Rezultate Evaluare ---")
    print(f"Test Accuracy: {acc:.4f}")
    print(f"Test F1-Score (Macro): {f1:.4f}")
    
    # Baseline Metrics (Hardcoded from Etapa 5 context for comparison)
    BASELINE_ACC = 0.72
    BASELINE_F1 = 0.68
    BASELINE_LATENCY = 48
    
    improvement_acc = ((acc - BASELINE_ACC) / BASELINE_ACC) * 100
    improvement_f1 = ((f1 - BASELINE_F1) / BASELINE_F1) * 100
    improvement_lat = ((latency_ms - BASELINE_LATENCY) / BASELINE_LATENCY) * 100
    
    # Salvare metrici JSON
    metrics = {
        "model": os.path.basename(model_path),
        "test_accuracy": float(acc),
        "test_f1_macro": float(f1),
        "test_precision_macro": float(precision),
        "test_recall_macro": float(recall),
        "false_negative_rate": float(FNR),
        "false_positive_rate": float(FPR),
        "inference_latency_ms": float(f"{latency_ms:.2f}"),
        "improvement_vs_baseline": {
            "accuracy": f"{improvement_acc:+.1f}%",
            "f1_score": f"{improvement_f1:+.1f}%",
            "latency": f"{improvement_lat:+.0f}%"
        },
        "classes": class_names
    }
    
    metrics_path = os.path.join(RESULTS_DIR, output_json)
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=4)
    print(f"Metrici extinse salvate în {metrics_path}")
    
    # Confusion Matrix
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title('Confusion Matrix')
    
    cm_path = os.path.join(DOCS_DIR, output_cm)
    plt.savefig(cm_path)
    print(f"Matricea de confuzie salvată în {cm_path}")
    plt.close()
    
    # Raport detaliat
    print("\n--- Raport Detaliat ---")
    print(classification_report(y_true, y_pred, target_names=class_names))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, default="models/trained_model.h5", help='Path to model')
    parser.add_argument('--json', type=str, default="test_metrics.json", help='Output JSON filename')
    parser.add_argument('--cm', type=str, default="confusion_matrix.png", help='Output Confusion Matrix filename')
    args = parser.parse_args()
    
    evaluate_model(args.model, args.json, args.cm)
