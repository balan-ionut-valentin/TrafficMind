import cv2
import os
import time
import uuid
import shutil

INPUT_DIR = "../../data/raw/phone_uploads"
OUTPUT_DIR = "../../data/generated"
PROCESSED_DIR = "../../data/raw/phone_uploads/done"
IMG_SIZE = (64, 64)

CLASSES = {
    ord('1'): "crosswalk",
    ord('2'): "noentry",
    ord('3'): "priorityroad",
    ord('4'): "roundabout",
    ord('5'): "speedlimit",
    ord('6'): "stop",
    ord('7'): "trafficlight",
    ord('8'): "yield"
}

drawing = False
ix, iy = -1, -1
bbox = None

def ensure_dirs():
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)
        print(f"Creat folder input: {INPUT_DIR}")
        print("-> Pune pozele de pe telefon aici!")
    
    if not os.path.exists(PROCESSED_DIR):
        os.makedirs(PROCESSED_DIR)

    for key in CLASSES:
        cls_path = os.path.join(OUTPUT_DIR, CLASSES[key])
        if not os.path.exists(cls_path):
            os.makedirs(cls_path)

def draw_rect(event, x, y, flags, param):
    global ix, iy, drawing, bbox
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        bbox = None

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            pass

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        bbox = (min(ix, x), min(iy, y), abs(ix - x), abs(iy - y))

def main():
    ensure_dirs()
    
    files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not files:
        print(f"Nu am gasit imagini in {INPUT_DIR}!")
        return

    print("=== TrafficMind Data Labeler ===")
    print("Instructiuni:")
    print("1. Trage cu mouse-ul un chenar peste semnul de circulatie.")
    print("2. Apasa tasta corespunzatoare clasei:")
    for k, v in CLASSES.items():
        print(f"   [{chr(k)}] -> {v}")
    print("3. Apasa 'SPACE' pentru a trece la urmatoarea poza (SKIP).")
    print("4. Apasa 'q' pentru a iesi.")
    print("================================")

    cv2.namedWindow('Labeler')
    cv2.setMouseCallback('Labeler', draw_rect)

    for filename in files:
        filepath = os.path.join(INPUT_DIR, filename)
        img = cv2.imread(filepath)
        
        if img is None:
            continue
            
        display_scale = 1.0
        h, w = img.shape[:2]
        if h > 800 or w > 1000:
            display_scale = min(800/h, 1000/w)
            img_display = cv2.resize(img, None, fx=display_scale, fy=display_scale)
        else:
            img_display = img.copy()
            
        original_img_display = img_display.copy()

        while True:
            temp_img = img_display.copy()
            
            if drawing:
                pass
                
            if bbox:
                x, y, w_box, h_box = bbox
                cv2.rectangle(temp_img, (x, y), (x + w_box, y + h_box), (0, 255, 0), 2)
                cv2.putText(temp_img, "Apasa tasta clasei (1-8)", (x, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            cv2.imshow('Labeler', temp_img)
            
            k = cv2.waitKey(20) & 0xFF

            if k == ord('q'):
                print("Iesire...")
                return

            if k == 32: 
                print(f"Skipped {filename}")
                break
                
            if k in CLASSES and bbox:
                x, y, w_box, h_box = bbox
                
                if w_box < 5 or h_box < 5:
                    print("Box prea mic!")
                    bbox = None
                    continue
                real_x = int(x / display_scale)
                real_y = int(y / display_scale)
                real_w = int(w_box / display_scale)
                real_h = int(h_box / display_scale)
                
                crop = img[real_y:real_y+real_h, real_x:real_x+real_w]
                
                if crop.size == 0:
                    continue
                crop_resized = cv2.resize(crop, IMG_SIZE)
                
                class_name = CLASSES[k]
                out_name = f"{int(time.time())}_{uuid.uuid4().hex[:6]}.png"
                out_path = os.path.join(OUTPUT_DIR, class_name, out_name)
                
                cv2.imwrite(out_path, crop_resized)
                print(f"Salvat: {class_name} -> {out_name}")
                
                shutil.move(filepath, os.path.join(PROCESSED_DIR, filename))
                bbox = None
                break 
    cv2.destroyAllWindows()
    print("Toate pozele au fost procesate.")

if __name__ == "__main__":
    main()
