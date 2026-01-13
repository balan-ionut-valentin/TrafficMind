import os
import xml.etree.ElementTree as ET
import cv2
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from shutil import copyfile
import numpy as np

BASE_DIR = "data"
RAW_IMAGES = os.path.join(BASE_DIR, "raw/images")
RAW_ANNOTATIONS = os.path.join(BASE_DIR, "raw/annotations")
OUTPUT_DIR = os.path.join(BASE_DIR, "processed")

IMG_SIZE = (64, 64) 

def parse_annotations():
    """Citește toate XML-urile și extrage informațiile."""
    data = []
    xml_files = [f for f in os.listdir(RAW_ANNOTATIONS) if f.endswith('.xml')]
    
    print(f"Procesare {len(xml_files)} fișiere XML...")
    
    for xml_file in xml_files:
        tree = ET.parse(os.path.join(RAW_ANNOTATIONS, xml_file))
        root = tree.getroot()
        
        filename = root.find('filename').text
        if not os.path.exists(os.path.join(RAW_IMAGES, filename)):
            continue
            
        for obj in root.findall('object'):
            label = obj.find('name').text
            bndbox = obj.find('bndbox')
            xmin = int(bndbox.find('xmin').text)
            ymin = int(bndbox.find('ymin').text)
            xmax = int(bndbox.find('xmax').text)
            ymax = int(bndbox.find('ymax').text)
            
            data.append([filename, label, xmin, ymin, xmax, ymax])
            
    df = pd.DataFrame(data, columns=['filename', 'label', 'xmin', 'ymin', 'xmax', 'ymax'])
    return df

def perform_eda(df):
    """Realizează Analiza Exploratorie a Datelor (EDA)."""
    print("\n--- ANALIZA EXPLORATORIE (EDA) ---")
    
    class_counts = df['label'].value_counts()
    print("Distribuția claselor:\n", class_counts)
    
    plt.figure(figsize=(10, 6))
    class_counts.plot(kind='bar', color='skyblue')
    plt.title('Distribuția Semnelor de Circulație')
    plt.xlabel('Clasă')
    plt.ylabel('Număr de imagini')
    plt.tight_layout()
    plt.savefig(os.path.join(BASE_DIR, 'distributie_clase.png'))    
    return class_counts

def save_and_split_data(df):
    """Împarte datele și salvează imaginile decupate."""
    print("\n--- PREPROCESARE ȘI SPLITTING ---")
    
    X = df.drop(columns=['label'])
    y = df['label']
    
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=42)
    
    datasets = {
        'train': (X_train, y_train),
        'validation': (X_val, y_val),
        'test': (X_test, y_test)
    }
    
    for split_name, (X_part, y_part) in datasets.items():
        print(f"Procesez setul: {split_name} ({len(X_part)} imagini)...")
        
        part_df = pd.concat([X_part, y_part], axis=1)
        
        for idx, row in part_df.iterrows():
            img_path = os.path.join(RAW_IMAGES, row['filename'])
            img = cv2.imread(img_path)
            
            if img is None:
                continue
            cropped_img = img[row['ymin']:row['ymax'], row['xmin']:row['xmax']]
            try:
                resized_img = cv2.resize(cropped_img, IMG_SIZE)
            except Exception as e:
                print(f"Eroare la redimensionare {row['filename']}: {e}")
                continue
            
            save_folder = os.path.join(OUTPUT_DIR, split_name, row['label'])
            os.makedirs(save_folder, exist_ok=True)
            
            save_path = os.path.join(save_folder, f"{os.path.splitext(row['filename'])[0]}_{idx}.png")
            cv2.imwrite(save_path, resized_img)

if __name__ == "__main__":
    df = parse_annotations()
    perform_eda(df)
    save_and_split_data(df)