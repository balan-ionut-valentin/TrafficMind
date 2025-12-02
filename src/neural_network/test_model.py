import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

BASE_DIR = "../../data/processed"
TEST_DIR = os.path.join(BASE_DIR, "test")
MODEL_PATH = "traffic_sign_model.h5"
IMG_SIZE = (64, 64)
BATCH_SIZE = 32

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

def visualize_results(model, test_ds, class_names):
    # Iterăm prin toate batch-urile din setul de testare
    for batch_id, (images, labels) in enumerate(test_ds):
        
        # Facem predicția pe tot batch-ul curent (32 imagini)
        predictions = model.predict(images, verbose=0)
        predicted_ids = np.argmax(predictions, axis=1)
        true_ids = np.argmax(labels, axis=1)
        
        plt.figure(figsize=(10, 10))
        plt.suptitle(f"Batch {batch_id + 1}", fontsize=16)
        num_to_show = min(9, len(images))

        for i in range(num_to_show): 
            ax = plt.subplot(3, 3, i + 1)
            plt.imshow(images[i].numpy().astype("uint8"))
            
            pred_label = class_names[predicted_ids[i]]
            true_label = class_names[true_ids[i]]
            confidence = 100 * np.max(predictions[i])
            
            color = 'green' if predicted_ids[i] == true_ids[i] else 'red'
            
            plt.title(f"Pred: {pred_label} ({confidence:.1f}%)\nReal: {true_label}", 
                      color=color, fontsize=10)
            plt.axis("off")
        
        plt.tight_layout()
        plt.show()

        user_input = input("Apasă ENTER pentru următoarele 9 imagini (sau scrie 'q' pentru a ieși): ")
        if user_input.lower() == 'q':
            print("Vizualizare oprită.")
            break
if __name__ == "__main__":
    if not os.path.exists(MODEL_PATH):
        print("Eroare: Fișierul .h5 nu a fost găsit! Rulează train_model.py.")
        exit()

    print("Încărcare model...")
    model = tf.keras.models.load_model(MODEL_PATH)
    
    test_ds, class_names = load_test_data()
    
    print("\nEvaluare pe setul de TEST...")
    loss, accuracy = model.evaluate(test_ds)
    print(f"\n-------------------------------")
    print(f"Acuratețe finală: {accuracy * 100:.2f}%")
    print(f"Eroare (Loss): {loss:.4f}")
    print(f"-------------------------------\n")
    
    visualize_results(model, test_ds, class_names)