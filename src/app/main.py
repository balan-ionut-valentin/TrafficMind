import cv2
import numpy as np
import tensorflow as tf
import os
import argparse
import time

# Configuration
DEFAULT_MODEL_PATH = "../../models/optimized_model.h5"
FALLBACK_MODEL_PATH = "../../models/trained_model.h5"
IMG_SIZE = (64, 64)

# Classes in alphabetical order (must match training)
CLASS_NAMES = ['Crosswalk', 'NoEntry', 'PriorityRoad', 'Roundabout', 'Speedlimit', 'Stop', 'Trafficlight', 'Yield']

# State Machine Configuration
CONFIDENCE_THRESHOLD = 0.60
CRITICAL_SIGNS = ['Stop', 'NoEntry', 'Trafficlight', 'Yield']
STATE_NORMAL = "NORMAL"
STATE_ALERT = "ALERT"
STATE_UNCERTAIN = "UNCERTAIN"

def preprocess_frame(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resized_frame = cv2.resize(rgb_frame, IMG_SIZE)
    # Normalize if the model expects [0,1]. build_cnn_model has Rescaling(1./255) inside, so input is 0-255 uint8 or float.
    # But usually cv2 returns uint8. The Rescaling layer handles it.
    input_data = np.expand_dims(resized_frame, axis=0)
    return input_data

def draw_ui(frame, label, confidence, state, processing_time_ms):
    height, width, _ = frame.shape
    
    # Colors
    COLOR_RED = (0, 0, 255)
    COLOR_GREEN = (0, 255, 0)
    COLOR_YELLOW = (0, 255, 255)
    COLOR_BLACK = (0, 0, 0)
    
    color = COLOR_GREEN
    if state == STATE_ALERT:
        color = COLOR_RED
    elif state == STATE_UNCERTAIN:
        color = COLOR_YELLOW
        
    # Draw top banner
    cv2.rectangle(frame, (0, 0), (width, 80), (0, 0, 0), -1)
    
    # Draw Label
    text = f"Class: {label} [{state}]"
    cv2.putText(frame, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    
    # Draw Confidence Bar
    bar_x = 20
    bar_y = 55
    bar_w = 300
    bar_h = 15
    fill_w = int(bar_w * (confidence / 100))
    
    cv2.rectangle(frame, (bar_x, bar_y), (bar_x + bar_w, bar_y + bar_h), (50, 50, 50), -1)
    cv2.rectangle(frame, (bar_x, bar_y), (bar_x + fill_w, bar_y + bar_h), color, -1)
    cv2.putText(frame, f"{confidence:.1f}%", (bar_x + bar_w + 10, bar_y + 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    # Draw Latency
    cv2.putText(frame, f"Latency: {processing_time_ms:.1f}ms", (width - 200, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)
    
    return frame

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, default=DEFAULT_MODEL_PATH, help='Path to model file')
    args = parser.parse_args()

    model_path = args.model
    if not os.path.exists(model_path):
        print(f"Warning: Model not found at {model_path}.")
        if os.path.exists(FALLBACK_MODEL_PATH):
            print(f"Falling back to {FALLBACK_MODEL_PATH}")
            model_path = FALLBACK_MODEL_PATH
        else:
            print("Error: No model found.")
            return

    print(f"Loading model: {model_path}...")
    try:
        model = tf.keras.models.load_model(model_path)
    except Exception as e:
        print(f"Error loading model: {e}")
        return
        
    print("Model loaded. Starting camera...")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    print("Press Q to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        start_time = time.time()
        
        # ROI Logic (Center Crop)
        h, w, _ = frame.shape
        box_size = 300
        x1 = int(w/2 - box_size/2)
        y1 = int(h/2 - box_size/2)
        x2 = int(w/2 + box_size/2)
        y2 = int(h/2 + box_size/2)
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)
        roi = frame[y1:y2, x1:x2]
        
        label = "Waiting..."
        confidence = 0.0
        state = STATE_NORMAL
        
        if roi.size > 0:
            input_data = preprocess_frame(roi)
            
            # Interference
            predictions = model.predict(input_data, verbose=0)
            class_id = np.argmax(predictions[0])
            confidence = 100 * np.max(predictions[0])
            label = CLASS_NAMES[class_id]
            
            # State Machine Logic
            if confidence < (CONFIDENCE_THRESHOLD * 100):
                state = STATE_UNCERTAIN
                label = "Unknown/Uncertain"
            else:
                if label in CRITICAL_SIGNS:
                    state = STATE_ALERT
                else:
                    state = STATE_NORMAL
        
        end_time = time.time()
        latency = (end_time - start_time) * 1000
        
        draw_ui(frame, label, confidence, state, latency)
        
        cv2.imshow('TrafficMind Etapa 6 - Optimized', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()