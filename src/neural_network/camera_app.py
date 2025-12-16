import cv2
import numpy as np
import tensorflow as tf
import os

MODEL_PATH = "../../models/trained_model.h5"
IMG_SIZE = (64, 64)

# Lista în ordinea alfabetică a claselor
CLASS_NAMES = ['Crosswalk', 'NoEntry', 'PriorityRoad', 'Roundabout', 'Speedlimit', 'Stop', 'Trafficlight', 'Yield']

def preprocess_frame(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Redimensionare la 64x64 
    resized_frame = cv2.resize(rgb_frame, IMG_SIZE)
    
    input_data = np.expand_dims(resized_frame, axis=0)
    
    return input_data

def main():
    if not os.path.exists(MODEL_PATH):
        print("Eroare: Nu a fost găsit modelul .h5!")
        return

    print("Încărcare model neuronal...")
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model încărcat! Pornire camera...")

    cap = cv2.VideoCapture(0) # 0 pentru camera web implicită

    if not cap.isOpened():
        print("Eroare: Camera web nu poate fi deschisă")
        return

    # Setare dimensiuni fereastră
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while True:
        # Citim un cadru
        ret, frame = cap.read()
        if not ret:
            break

        height, width, _ = frame.shape
        box_size = 300
        x1 = int(width/2 - box_size/2)
        y1 = int(height/2 - box_size/2)
        x2 = int(width/2 + box_size/2)
        y2 = int(height/2 + box_size/2)
        
        # Desenăm pătratul pe ecran
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)
        
        # Extragem imaginea din pătrat pentru analiză
        roi = frame[y1:y2, x1:x2]
        
        # Dacă ROI e valid, facem predicția
        if roi.size > 0:
            input_data = preprocess_frame(roi)
            
            # Predicția
            predictions = model.predict(input_data, verbose=0)
            score = tf.nn.softmax(predictions[0])
            class_id = np.argmax(predictions[0])
            confidence = 100 * np.max(predictions[0])
            
            label_text = CLASS_NAMES[class_id]
            
            # Afișăm rezultatul doar dacă e sigur > 70%
            if confidence > 70:
                color = (0, 255, 0) # Verde
                text = f"{label_text}: {confidence:.1f}%"
            else:
                color = (0, 0, 255) # Roșu
                text = "Not found"
                
            cv2.putText(frame, text, (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        cv2.imshow('TrafficMind (Apasa Q pentru iesire)', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()