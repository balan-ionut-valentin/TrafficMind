import os
import shutil
from sklearn.model_selection import train_test_split
import glob

# Calea unde a salvat capture.py
SOURCE_DIR = "data/generated"
# Calea unde antreneaza train_model.py
DEST_DIR = "data/processed"

def merge():
    if not os.path.exists(SOURCE_DIR):
        print("Nu gasesc datele generate manual!")
        return

    classes = os.listdir(SOURCE_DIR)
    
    for cls in classes:
        src_path = os.path.join(SOURCE_DIR, cls)
        if not os.path.isdir(src_path): continue
            
        images = glob.glob(os.path.join(src_path, "*"))
        if not images: continue

        print(f"Procesez clasa {cls} ({len(images)} imagini noi)...")

        train, temp = train_test_split(images, test_size=0.2, random_state=42)
        val, test = train_test_split(temp, test_size=0.5, random_state=42)

        for split, imgs in [("train", train), ("validation", val), ("test", test)]:
            dest_path = os.path.join(DEST_DIR, split, cls)
            os.makedirs(dest_path, exist_ok=True)
            
            for img in imgs:
                shutil.copy(img, os.path.join(dest_path, os.path.basename(img)))

if __name__ == "__main__":
    merge()