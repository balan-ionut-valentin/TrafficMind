# Modul 3: Interfață Utilizator (UI)

Acest modul asigură interacțiunea cu utilizatorul și vizualizarea predicțiilor în timp real.

## Descriere
Aplicația utilizează fluxul video de la camera web, detectează ROI (Region of Interest) și folosește rețeaua neuronală antrenată pentru a clasifica semnele de circulație.

## Fișiere Relevante
*   **Cod sursă:** `src/neural_network/camera_app.py`
*   **Model încărcat:** `models/trained_model.h5`

## Instrucțiuni de Lansare

Pentru a porni aplicația, rulați următoarea comandă din rădăcina proiectului:

```bash
python src/neural_network/camera_app.py
```

### Cerințe
*   Camera web funcțională conectată.
*   Bibliotecile instalate (`pip install -r requirements.txt`).
*   Modelul antrenat existent (`models/trained_model.h5`).

## Instrucțiuni de Lansare fără fișier (`models/trained_model.h5`)

Pentru a porni aplicația, rulați următoarea comandă din rădăcina proiectului:

```bash
python src/preprocessing/process_data.py
python src/data_acquisition/camera.py
python src/preprocessing/merge_data.py
python src/neural_network/train_model.py --epochs 50 --batch_size 32 --early_stopping
python src/neural_network/evaluate.py --model models/trained_model.h5
python src/neural_network/camera_app.py
```

## Funcționalități
1.  **Captură Video:** Preia imagini frame-by-frame.
2.  **Preprocesare:** Redimensionează și normalizează imaginea centrală.
3.  **Inferență:** Rulează predicția modelului CNN.
4.  **Afișare:** Suprapune clasa prezisă și scorul de încredere pe imagine.
