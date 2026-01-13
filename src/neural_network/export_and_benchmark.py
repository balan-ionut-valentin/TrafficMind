import tensorflow as tf
import time
import numpy as np
import os

MODEL_PATH = "models/trained_model.h5"
TFLITE_PATH = "models/model.tflite"

def convert_to_tflite():
    print(f"Încărcare model din {MODEL_PATH}...")
    model = tf.keras.models.load_model(MODEL_PATH)
    
    print("Conversie către TFLite...")
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()
    
    with open(TFLITE_PATH, 'wb') as f:
        f.write(tflite_model)
    print(f"Model TFLite salvat în {TFLITE_PATH}")
    return TFLITE_PATH

def benchmark_tflite(model_path):
    print("\nÎncepe Benchmark TFLite...")
    
    # Încărcare interpretor
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    input_shape = input_details[0]['shape']
    print(f"Input Shape: {input_shape}")
    
    # Generare date dummy
    input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
    
    # Warm-up (primele rulări sunt mai lente)
    print("Warm-up...")
    for _ in range(10):
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()
        
    # Benchmark real
    iterations = 100
    print(f"Rulare {iterations} de iterații...")
    
    start_time = time.time()
    for _ in range(iterations):
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()
    end_time = time.time()
    
    avg_time = (end_time - start_time) / iterations * 1000 # ms
    print(f"\n--- Rezultat Benchmark ---")
    print(f"Latență medie: {avg_time:.2f} ms")
    
    if avg_time < 50:
        print("Status: SUCCES (< 50ms)")
    else:
        print("Status: LENT (> 50ms)")

if __name__ == "__main__":
    if not os.path.exists(MODEL_PATH):
        print(f"Eroare: Nu găsesc {MODEL_PATH}")
    else:
        try:
            tflite_path = convert_to_tflite()
            benchmark_tflite(tflite_path)
        except Exception as e:
            print(f"Eroare: {e}")
