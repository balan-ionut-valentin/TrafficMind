import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import random

MODEL_PATH = "models/optimized_model.h5"
TEST_DIR = "data/processed/test"
OUTPUT_PATH = "docs/results/example_predictions.png"
IMG_SIZE = (64, 64)

def generate_example_grid():
    if not os.path.exists(MODEL_PATH):
        print(f"Error: Model not found at {MODEL_PATH}")
        return

    print("Loading model...")
    model = tf.keras.models.load_model(MODEL_PATH)
    
    print("Loading test data...")
    test_ds = tf.keras.utils.image_dataset_from_directory(
        TEST_DIR,
        image_size=IMG_SIZE,
        batch_size=32,
        label_mode='categorical',
        shuffle=True
    )
    class_names = test_ds.class_names
    
    # Collect images and predictions
    images_batch = []
    labels_batch = []
    preds_batch = []
    
    for images, labels in test_ds:
        preds = model.predict(images, verbose=0)
        images_batch.append(images.numpy())
        labels_batch.append(labels.numpy())
        preds_batch.append(preds)
        # We only need a few batches to find examples
        if len(images_batch) * 32 > 100: 
            break
            
    images = np.concatenate(images_batch)
    labels = np.concatenate(labels_batch)
    preds = np.concatenate(preds_batch)
    
    true_indices = np.argmax(labels, axis=1)
    pred_indices = np.argmax(preds, axis=1)
    
    # Identify correct and incorrect
    correct_mask = (true_indices == pred_indices)
    incorrect_mask = (true_indices != pred_indices)
    
    correct_idxs = np.where(correct_mask)[0]
    incorrect_idxs = np.where(incorrect_mask)[0]
    
    print(f"Found {len(correct_idxs)} correct and {len(incorrect_idxs)} incorrect examples.")
    
    # Select 9 examples (aim for mix, e.g., 5 correct, 4 incorrect if available)
    selected_idxs = []
    
    n_incorrect = min(4, len(incorrect_idxs))
    if n_incorrect > 0:
        selected_idxs.extend(np.random.choice(incorrect_idxs, n_incorrect, replace=False))
        
    n_correct = 9 - len(selected_idxs)
    selected_idxs.extend(np.random.choice(correct_idxs, n_correct, replace=False))
    
    # Plot
    plt.figure(figsize=(10, 10))
    for i, idx in enumerate(selected_idxs):
        ax = plt.subplot(3, 3, i + 1)
        img = images[idx].astype("uint8")
        true_label = class_names[true_indices[idx]]
        pred_label = class_names[pred_indices[idx]]
        confidence = 100 * np.max(preds[idx])
        
        color = 'green' if true_indices[idx] == pred_indices[idx] else 'red'
        
        plt.imshow(img)
        plt.title(f"True: {true_label}\nPred: {pred_label} ({confidence:.1f}%)", color=color, fontsize=9)
        plt.axis("off")
        
    plt.tight_layout()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    plt.savefig(OUTPUT_PATH)
    print(f"Saved example grid to {OUTPUT_PATH}")
    plt.close()

if __name__ == "__main__":
    generate_example_grid()
