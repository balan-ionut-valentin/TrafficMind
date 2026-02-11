## 1. Identificare Proiect

| Câmp | Valoare |
|------|---------|
| **Student** | Balan Ionut-Valentin |
| **Grupa / Specializare** | 631AB / Informatică Industrială |
| **Disciplina** | Rețele Neuronale |
| **Instituție** | POLITEHNICA București – FIIR |
| **Link Repository GitHub** | https://github.com/balan-ionut-valentin/TrafficMind |
| **Acces Repository** | [Privat cu acces cadre didactice RN] |
| **Stack Tehnologic** | [Python / Keras / TensorFlow] |
| **Domeniul Industrial de Interes (DII)** | [Automotive / Asistență Șofer] |
| **Tip Rețea Neuronală** | [CNN (Convolutional Neural Network)] |

### Rezultate Cheie (Versiunea Finală vs Etapa 6)

| Metric | Țintă Minimă | Rezultat Etapa 6 | Rezultat Final | Îmbunătățire | Status |
|--------|--------------|------------------|----------------|--------------|--------|
| Accuracy (Test Set) | ≥70% | 94.00% | 95.31% | +1.31% | [✓] |
| F1-Score (Macro) | ≥0.65 | 0.91 | 0.92 | +0.01 | [✓] |
| Latență Inferență | <100ms | 60 ms | 51.2 ms | -8.8 ms | [✓] |
| Contribuție Date Originale | ≥40% | 40% | 40% | - | [✓] |
| Nr. Experimente Optimizare | ≥4 | 4 | 5 | +1 | [✓] |

### Declarație de Originalitate & Politica de Utilizare AI

**Acest proiect reflectă munca, gândirea și deciziile mele proprii.**

Utilizarea asistenților de inteligență artificială (ChatGPT, Claude, Grok, GitHub Copilot etc.) este **permisă și încurajată** ca unealtă de dezvoltare – pentru explicații, generare de idei, sugestii de cod, debugging, structurarea documentației sau rafinarea textelor.

**Nu este permis** să preiau:
- cod, arhitectură RN sau soluție luată aproape integral de la un asistent AI fără modificări și raționamente proprii semnificative,
- dataset-uri publice fără contribuție proprie substanțială (minimum 40% din observațiile finale – conform cerinței obligatorii Etapa 4),
- conținut esențial care nu poartă amprenta clară a propriei mele înțelegeri.

**Confirmare explicită (bifez doar ce este adevărat):**

| Nr. | Cerință                                                                 | Confirmare |
|-----|-------------------------------------------------------------------------|------------|
| 1   | Modelul RN a fost antrenat **de la zero** (weights inițializate random, **NU** model pre-antrenat descărcat) | [x] DA     |
| 2   | Minimum **40% din date sunt contribuție originală** (generate/achiziționate/etichetate de mine) | [x] DA     |
| 3   | Codul este propriu sau sursele externe sunt **citate explicit** în Bibliografie | [x] DA     |
| 4   | Arhitectura, codul și interpretarea rezultatelor reprezintă **muncă proprie** (AI folosit doar ca tool, nu ca sursă integrală de cod/dataset) | [x] DA     |
| 5   | Pot explica și justifica **fiecare decizie importantă** cu argumente proprii | [x] DA     |

**Semnătură student (prin completare):** Declar pe propria răspundere că informațiile de mai sus sunt corecte.
*Balan Ionut-Valentin*

---

## 2. Descrierea Nevoii și Soluția SIA

### 2.1 Nevoia Reală / Studiul de Caz

În contextul traficului rutier tot mai aglomerat, neatenția șoferilor și vizibilitatea redusă a indicatoarelor rutiere reprezintă cauze majore ale accidentelor. Proiectul se adresează nevoii de sisteme avansate de asistență a șoferului (ADAS) care să monitorizeze activ mediul înconjurător și să ofere avertizări în timp real.
Situația actuală implică adesea decizii umane eronate cauzate de oboseală sau neatenție. O soluție automatizată care detectează și clasifică semnele de circulație (Stop, Cedează Trecerea, Limite de Viteză etc.) poate reduce semnificativ riscurile, alertând șoferul înainte de a intra într-o intersecție sau de a depăși viteza legală.

### 2.2 Beneficii Măsurabile Urmărite

1. **Reducerea timpului de reacție** al șoferului prin pre-alertare (Latență sistem < 100ms).
2. **Acuratețe ridicată** în identificarea semnelor critice (>95% pentru Stop/NoEntry).
3. **Disponibilitate 24/7** și robustețe la factori de oboseală umană.
4. **Scăderea ratei incidentelor** cauzate de neobservarea semnalizării rutiere.

### 2.3 Tabel: Nevoie → Soluție SIA → Modul Software

| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul** | **Modul software responsabil** | **Metric măsurabil** |
|---------------------------|--------------------------|--------------------------------|----------------------|
| Asistență șofer identificare semne | Detecție și clasificare în timp real | RN + Camera App | < 60ms/frame latență |
| Avertizare la semne critice (Stop) | Alertă vizuală accentuată (Roșu) | Camera App Logic + Inference | > 95% Recall pe clasa Stop |
| Îmbunătățire continuă date trafic | Colectare si etichetare date noi | Data Acquisition Module | > 15,000 imagini colectate |

---

## 3. Dataset și Contribuție Originală

### 3.1 Sursa și Caracteristicile Datelor

| Caracteristică | Valoare |
|----------------|---------|
| **Origine date** | [Mixt: Kaggle + Senzori Proprii] |
| **Sursa concretă** | Kaggle GTSRB + Imagini colectate cu telefonul mobil |
| **Număr total observații finale (N)** | 16,500 (aprox) |
| **Număr features** | Imagine 64x64 pixeli RGB (3 canale) |
| **Tipuri de date** | Imagini |
| **Format fișiere** | PNG / CSV (labels) |
| **Perioada colectării/generării** | Noiembrie 2025 - Ianuarie 2026 |

### 3.2 Contribuția Originală (minim 40% OBLIGATORIU)

| Câmp | Valoare |
|------|---------|
| **Total observații finale (N)** | 16,500 |
| **Observații originale (M)** | 6,600 |
| **Procent contribuție originală** | 40% |
| **Tip contribuție** | Senzori proprii (Captură foto) + Etichetare manuală |
| **Locație cod generare** | `src/data_acquisition/capture.py` |
| **Locație date originale** | `data/generated/` |

**Descriere metodă generare/achiziție:**

Pentru a asigura robustețea modelului în condiții specifice traficului local, am completat setul de date public cu imagini proprii. Acestea au fost achiziționate folosind camera telefonului mobil, în diverse condiții de iluminare (zi, înnorat, amurg) și din unghiuri variate (față, lateral) pentru a simula perspectiva unui vehicul în mișcare. Imaginile au fost decupate (crop) și etichetate manual.

### 3.3 Preprocesare și Split Date

| Set | Procent | Număr Observații |
|-----|---------|------------------|
| Train | 70% | ~11,550 |
| Validation | 15% | ~2,475 |
| Test | 15% | ~2,475 |

**Preprocesări aplicate:**
- **Redimensionare:** Toate imaginile aduse la 64x64 pixeli.
- **Normalizare:** Scalare valori pixeli [0, 255] -> [0, 1].
- **One-Hot Encoding:** Transformarea etichetelor categoriale în vectori binari.
- **Shuffle:** Amestecare aleatorie pentru a preveni bias-ul de ordine.

**Referințe fișiere:** `data/README.md`, `config/preprocessing_params.pkl`

---

## 4. Arhitectura SIA și State Machine

### 4.1 Cele 3 Module Software

| Modul | Tehnologie | Funcționalitate Principală | Locație în Repo |
|-------|------------|---------------------------|-----------------|
| **Data Logging / Acquisition** | Python (OpenCV) | Achiziție imagini, etichetare și salvare | `src/data_acquisition/` |
| **Neural Network** | Keras/TensorFlow | Definire model, antrenare, optimizare | `src/neural_network/` |
| **Web Service / UI** | Streamlit | Interfață utilizator pentru inferență live | `src/app/` |

### 4.2 State Machine

**Locație diagramă:** `docs/state_machine.png`

**Stări principale și descriere:**

| Stare | Descriere | Condiție Intrare | Condiție Ieșire |
|-------|-----------|------------------|-----------------|
| `INIT` | Încărcare model și configurare cameră | Start aplicație | Model & Camera OK |
| `CAPTURE` | Preluare frame curent de la cameră | Loop activ | Frame disponibil |
| `PREPROCESS` | Resize 64x64 și normalizare | Frame capturat | Date gata de inferență |
| `INFERENCE` | Rulare model.predict() | Date preprocesate | Predicție (probabilități) |
| `FILTER` | Verificare prag încredere (Confidence Check) | Predicție disponibilă | Decizie validată |
| `DISPLAY` | Afișare bounding box și etichetă | Decizie luată | Așteptare frame nou |

**Justificare alegere arhitectură State Machine:**

Aplicația este un flux continuu (real-time loop) critic pentru siguranța auto. Structura secvențială cu stări distincte permite izolarea erorilor (ex: dacă camera eșuează, nu se intră în inferență) și asigură o latență minimă. Starea de `FILTER` este esențială pentru a nu afișa detecții false ("zgomot") când încrederea modelului este mică.

### 4.3 Actualizări State Machine în Etapa 6

| Componentă Modificată | Valoare Etapa 5 | Valoare Etapa 6 | Justificare Modificare |
|----------------------|-----------------|-----------------|------------------------|
| Threshold alertă | 0.50 | 0.60 | Reducerea alarmelor false (False Positives) |
| Stare nouă | - | `UNCERTAIN` | Gestionare cazuri cu încredere < 0.60 |
| Feedback UI | Text simplu | Confidence Bar | Vizualizare clară a certitudinii deciziei |

---

## 5. Modelul RN – Antrenare și Optimizare

### 5.1 Arhitectura Rețelei Neuronale

```
Input (64, 64, 3)
  → Conv2D(32, 3x3, ReLU) → MaxPool(2x2)
  → Conv2D(64, 3x3, ReLU) → MaxPool(2x2)
  → Conv2D(64, 3x3, ReLU) → MaxPool(2x2)
  → Flatten
  → Dense(64, ReLU) → Dropout(0.5)
  → Dense(8, Softmax)
Output: 8 clase
```

**Justificare alegere arhitectură:**
Am ales o arhitectură CNN cu 3 blocuri convoluționale (Deep CNN) deoarece este standardul de aur pentru procesarea imaginilor. Adâncimea rețelei permite extragerea caracteristicilor complexe (forme, texturi), iar Dropout-ul de 0.5 previne overfitting-ul, esențial având în vedere dimensiunea moderată a setului de date.

### 5.2 Hiperparametri Finali (Model Optimizat - Etapa 6)

| Hiperparametru | Valoare Finală | Justificare Alegere |
|----------------|----------------|---------------------|
| Learning Rate | 0.001 (start) | Redus dinamic cu ReduceLROnPlateau pentru convergență fină |
| Batch Size | 32 | Balans optim între viteza de calcul și stabilitatea gradientului |
| Epochs | 50 | Early Stopping a oprit antrenarea la epoca ~35 pentru a evita overfitting |
| Optimizer | Adam | Convergență rapidă și adaptivă |
| Loss Function | Categorical Crossentropy | Problemă de clasificare multi-clasă |
| Regularizare | Dropout 0.5 | Forțează redundanța în rețea, crescând robustețea |

### 5.3 Experimente de Optimizare (minim 4 experimente)

| Exp# | Modificare față de Baseline | Accuracy | F1-Score | Timp Antrenare | Observații |
|------|----------------------------|----------|----------|----------------|------------|
| **Baseline** | Configurația Etapa 5 | 92.50% | 0.89 | 15 min | Model inițial solid |
| Exp 1 | LR 0.001 → 0.0001 | 91.80% | 0.88 | 18 min | Convergență prea lentă |
| Exp 2 | Batch 32 → 64 | 91.50% | 0.87 | 12 min | Scădere ușoară în generalizare |
| Exp 3 | Adăugare strat Dense 128 | 93.20% | 0.90 | 20 min | Îmbunătățire marginală, cost calcul |
| Exp 4 | Dropout 0.3 → 0.5 | 94.10% | 0.91 | 16 min | Reducere vizibilă overfitting |
| Exp 5 | **Augmentare Date (Rotation/Zoom)** | **95.31%** | **0.92** | 25 min | **Cea mai mare creștere de performanță** |
| **FINAL** | Exp 5 (Augmentat + Dropout 0.5) | **95.31%** | **0.92** | 25 min | **Modelul folosit în producție** |

**Justificare alegere model final:**
Configurația din Experimentul 5 a oferit cel mai bun echilibru. Introducerea augmentării datelor (rotații ușoare, zoom, variații de luminozitate) a forțat modelul să învețe caracteristici invariante, simulând mai bine condițiile reale de trafic unde semnele nu sunt întotdeauna perfect centrate sau iluminate.

**Referințe fișiere:** `results/optimization_experiments.csv`, `models/optimized_model.h5`

---

## 6. Performanță Finală și Analiză Erori

### 6.1 Metrici pe Test Set (Model Optimizat)

| Metric | Valoare | Target Minim | Status |
|--------|---------|--------------|--------|
| **Accuracy** | 95.31% | ≥70% | [✓] |
| **F1-Score (Macro)** | 0.92 | ≥0.65 | [✓] |
| **Precision (Macro)** | 0.95 | - | - |
| **Recall (Macro)** | 0.91 | - | - |

**Îmbunătățire față de Baseline (Etapa 5):**

| Metric | Etapa 5 (Baseline) | Etapa 6 (Optimizat) | Îmbunătățire |
|--------|-------------------|---------------------|--------------|
| Accuracy | 94.00% | 95.31% | +1.31% |
| F1-Score | 0.91 | 0.92 | +0.01 |

**Referință fișier:** `results/final_metrics.json`

### 6.2 Confusion Matrix

**Locație:** `docs/confusion_matrix_optimized.png`

**Interpretare:**

| Aspect | Observație |
|--------|------------|
| **Clasa cu cea mai bună performanță** | **Trafficlight** - Precision 100%, Recall 100%. Ușor de distins prin culoare/formă. |
| **Clasa cu cea mai slabă performanță** | **Speedlimit** - Confundat uneori cu alte semne circulare, Recall ~88%. |
| **Confuzii frecvente** | **Roundabout vs PriorityRoad**: Forme similare (romboidal vs pătrat rotit) și culori care pot părea similare în rezoluție mică. |
| **Dezechilibru clase** | Clasele **Yield** și **Stop** au performanțe bune, dar erorile rare sunt critice de analizat. |

### 6.3 Analiza Top 5 Erori

| # | Input | Predicție RN | Clasă Reală | Cauză Probabilă | Implicație Industrială |
|---|-------|--------------|-------------|-----------------|------------------------|
| 1 | Imagine încețoșată (motion blur) | NoEntry | Speedlimit | Pierderea detaliilor cifrelor la 64x64px | Citire greșită a vitezei -> risc amendă/accident |
| 2 | Semn parțial obturat de copac | Roundabout | Stop | Ocluzia formei octogonale caracteristice | **Critic:** Vehiculul nu oprește la STOP |
| 3 | Reflexie puternică soare | Speedlimit | Yield | Suptaexpunere (albire) a triunghiului roșu | Confuzie prioritate -> Risc coliziune |
| 4 | Unghi extrem (>45 grade) | PriorityRoad | Roundabout | Distorsionare geometrică a rombului | Eroare navigare (nu critic siguranță) |
| 5 | Imagine întunecată (seară) | Background | NoEntry | Lipsă contrast, semn neidentificat | Intrare pe sens interzis -> **Critic** |

### 6.4 Validare în Context Industrial

**Ce înseamnă rezultatele pentru aplicația reală:**
Cu un Recall de ~92%, sistemul detectează corect majoritatea semnelor. Totuși, rata de 8% False Negatives (semne ratate/confundate), deși acceptabilă pentru un sistem de *asistență* (unde șoferul are responsabilitate finală), nu este suficientă pentru *conducere autonomă* (Level 4/5).
Costul erorilor de tip "Stop ratat" (False Negative) este infinit mai mare decât o alarmă falsă (False Positive).

**Pragul de acceptabilitate pentru domeniu:** Recall ≥ 95% pentru semne critice (Stop/NoEntry).
**Status:** **Atins parțial** (Stop are recall bun, dar Speedlimit trage media în jos).
**Plan de îmbunătățire:** Colectare date low-light și antrenare specifică pe 'hard examples'.

---

## 7. Aplicația Software Finală

### 7.1 Modificări Implementate în Etapa 6

| Componentă | Stare Etapa 5 | Modificare Etapa 6 | Justificare |
|------------|---------------|-------------------|-------------|
| **Model încărcat** | `trained_model.h5` | `optimized_model.h5` | Acuratețe și robustețe superioară (+1.31%) |
| **Threshold decizie** | 0.50 default | 0.60 | Filtrare mai agresivă a predicțiilor incerte |
| **UI - feedback vizual** | Text simplu | Bară progres colorată (Confidence) | Informare intuitivă a gradului de siguranță |
| **Stare nouă** | N/A | `UNCERTAIN` | Tratare explicită a cazurilor 'la limită' |

### 7.2 Screenshot UI cu Model Optimizat

**Locație:** `docs/screenshots/inference_optimized.png`

**Descriere:** Screenshot-ul arată interfața aplicației rulând pe o imagine de test "Stop". Se observă predicția corectă "Stop", bara de încredere (Confidence) aproape plină (verde) și timpul de inferență (51ms) afișat în sidebar.

### 7.3 Demonstrație Funcțională End-to-End

**Locație dovadă:** `docs/demo/`

**Fluxul demonstrat:**

| Pas | Acțiune | Rezultat Vizibil |
|-----|---------|------------------|
| 1 | Input | Utilizatorul încarcă o imagine cu un semn "Yield" |
| 2 | Procesare | Imaginea este redimensionată și normalizată (invizibil, dar rapid) |
| 3 | Inferență | Modelul prezice clasa "Yield" cu 98% încredere |
| 4 | Decizie | UI afișează "Cedează Trecerea" și contur galben de avertizare |

**Latență măsurată end-to-end:** ~51.2 ms
**Data și ora demonstrației:** 20.01.2026

---

## 8. Structura Repository-ului Final

```
proiect-rn-balan-ionut-valentin/
│
├── README.md                               # ← ACEST FIȘIER (Overview Final Proiect - Pe moodle la Evaluare Finala RN > Upload Livrabil 1 - Proiect RN (Aplicatie Sofware) - trebuie incarcat cu numele: NUME_Prenume_Grupa_README_Proiect_RN.md)
│
├── docs/
│   ├── etapa3_analiza_date.md              # Documentație Etapa 3
│   ├── etapa4_arhitectura_SIA.md           # Documentație Etapa 4
│   ├── etapa5_antrenare_model.md           # Documentație Etapa 5
│   ├── etapa6_optimizare_concluzii.md      # Documentație Etapa 6
│   │
│   ├── state_machine.png                   # Diagrama State Machine inițială
│   ├── state_machine_v2.png                # (opțional) Versiune actualizată Etapa 6
│   ├── confusion_matrix_optimized.png      # Confusion matrix model final
│   │
│   ├── screenshots/
│   │   ├── ui_demo.png                     # Screenshot UI schelet (Etapa 4)
│   │   ├── inference_real.png              # Inferență model antrenat (Etapa 5)
│   │   └── inference_optimized.png         # Inferență model optimizat (Etapa 6)
│   │
│   ├── demo/                               # Demonstrație funcțională end-to-end
│   │   └── demo_end_to_end.gif             # (sau .mp4 / secvență screenshots)
│   │
│   ├── results/                            # Vizualizări finale
│   │   ├── loss_curve.png                  # Grafic loss/val_loss (Etapa 5)
│   │   ├── metrics_evolution.png           # Evoluție metrici (Etapa 6)
│   │   └── learning_curves_final.png       # Curbe învățare finale
│   │
│   └── optimization/                       # Grafice comparative optimizare
│       ├── accuracy_comparison.png         # Comparație accuracy experimente
│       └── f1_comparison.png               # Comparație F1 experimente
│
├── data/
│   ├── README.md                           # Descriere detaliată dataset
│   ├── raw/                                # Date brute originale
│   ├── processed/                          # Date curățate și transformate
│   ├── generated/                          # Date originale (contribuția ≥40%)
│   ├── train/                              # Set antrenare (70%)
│   ├── validation/                         # Set validare (15%)
│   └── test/                               # Set testare (15%)
│
├── src/
│   ├── data_acquisition/                   # MODUL 1: Generare/Achiziție date
│   │   ├── README.md                       # Documentație modul
│   │   ├── generate.py                     # Script generare date originale
│   │   └── [alte scripturi achiziție]
│   │
│   ├── preprocessing/                      # Preprocesare date (Etapa 3+)
│   │   ├── data_cleaner.py                 # Curățare date
│   │   ├── feature_engineering.py          # Extragere/transformare features
│   │   ├── data_splitter.py                # Împărțire train/val/test
│   │   └── combine_datasets.py             # Combinare date originale + externe
│   │
│   ├── neural_network/                     # MODUL 2: Model RN
│   │   ├── README.md                       # Documentație arhitectură RN
│   │   ├── model.py                        # Definire arhitectură (Etapa 4)
│   │   ├── train.py                        # Script antrenare (Etapa 5)
│   │   ├── evaluate.py                     # Script evaluare metrici (Etapa 5)
│   │   ├── optimize.py                     # Script experimente optimizare (Etapa 6)
│   │   └── visualize.py                    # Generare grafice și vizualizări
│   │
│   └── app/                                # MODUL 3: UI/Web Service
│       ├── README.md                       # Instrucțiuni lansare aplicație
│       └── main.py                         # Aplicație principală
│
├── models/
│   ├── optimized_model.h5                  # Model FINAL
│
├── results/
│   ├── training_history.csv                # Istoric antrenare - toate epocile (Etapa 5)
│   ├── test_metrics.json                   # Metrici baseline test set (Etapa 5)
│   ├── optimization_experiments.csv        # Toate experimentele optimizare (Etapa 6)
│   ├── final_metrics.json                  # Metrici finale model optimizat (Etapa 6)
│   └── error_analysis.json                 # Analiza detaliată erori (Etapa 6)
│
├── config/
│   ├── preprocessing_params.pkl            # Parametri preprocesare salvați (Etapa 3)
│   └── optimized_config.yaml               # Configurație finală model (Etapa 6)
│
├── requirements.txt                        # Dependențe Python (actualizat la fiecare etapă)
└── .gitignore                              # Fișiere excluse din versionare
```

### Legendă Progresie pe Etape

| Folder / Fișier | Etapa 3 | Etapa 4 | Etapa 5 | Etapa 6 |
|-----------------|:-------:|:-------:|:-------:|:-------:|
| `data/raw/`, `processed/`, `train/`, `val/`, `test/` | ✓ Creat | - | Actualizat* | - |
| `data/generated/` | - | ✓ Creat | - | - |
| `src/preprocessing/` | ✓ Creat | - | Actualizat* | - |
| `src/data_acquisition/` | - | ✓ Creat | - | - |
| `src/neural_network/model.py` | - | ✓ Creat | - | - |
| `src/neural_network/train.py`, `evaluate.py` | - | - | ✓ Creat | - |
| `src/neural_network/optimize.py`, `visualize.py` | - | - | - | ✓ Creat |
| `src/app/` | - | ✓ Creat | Actualizat | Actualizat |
| `models/untrained_model.*` | - | ✓ Creat | - | - |
| `models/trained_model.*` | - | - | ✓ Creat | - |
| `models/optimized_model.*` | - | - | - | ✓ Creat |
| `docs/state_machine.*` | - | ✓ Creat | - | (v2 opțional) |
| `docs/etapa3_analiza_date.md` | ✓ Creat | - | - | - |
| `docs/etapa4_arhitectura_SIA.md` | - | ✓ Creat | - | - |
| `docs/etapa5_antrenare_model.md` | - | - | ✓ Creat | - |
| `docs/etapa6_optimizare_concluzii.md` | - | - | - | ✓ Creat |
| `docs/confusion_matrix_optimized.png` | - | - | - | ✓ Creat |
| `docs/screenshots/` | - | ✓ Creat | Actualizat | Actualizat |
| `results/training_history.csv` | - | - | ✓ Creat | - |
| `results/optimization_experiments.csv` | - | - | - | ✓ Creat |
| `results/final_metrics.json` | - | - | - | ✓ Creat |
| **README.md** (acest fișier) | Draft | Actualizat | Actualizat | **FINAL** |

*\* Actualizat dacă s-au adăugat date noi în Etapa 4*

### Convenție Tag-uri Git

| Tag | Etapa | Commit Message Recomandat |
|-----|-------|---------------------------|
| `v0.3-data-ready` | Etapa 3 | "Etapa 3 completă - Dataset analizat și preprocesat" |
| `v0.4-architecture` | Etapa 4 | "Etapa 4 completă - Arhitectură SIA funcțională" |
| `v0.5-model-trained` | Etapa 5 | "Etapa 5 completă - Accuracy=X.XX, F1=X.XX" |
| `v0.6-optimized-final` | Etapa 6 | "Etapa 6 completă - Accuracy=X.XX, F1=X.XX (optimizat)" |

---

## 9. Instrucțiuni de Instalare și Rulare

### 9.1 Cerințe Preliminare
```
Python >= 3.8
pip >= 21.0
```

### 9.2 Instalare
```bash
# Creare mediu virtual (recomandat)
python -m venv venv
source venv/bin/activate        # Linux/Mac
sau: venv\Scripts\activate    # Windows
git clone https://github.com/balan-ionut-valentin/TrafficMind
cd TrafficMind
pip install -r requirements.txt
```

### 9.3 Rulare Pipeline Complet

```bash
# Lansare aplicație UI (Streamlit)
streamlit run src/app/main.py
```

### 9.4 Verificare Rapidă 
```bash
# Evaluare model final
python src/neural_network/evaluate.py --model models/optimized_model.h5
```

---

## 10. Concluzii și Discuții

### 10.1 Evaluare Performanță vs Obiective Inițiale

| Obiectiv Definit | Target | Realizat | Status |
|------------------|--------|----------|--------|
| Acuratețe detecție | ≥70% | 95.31% | [✓] |
| Timp răspuns | <100ms | 51.2ms | [✓] |
| Sistem funcțional end-to-end | Da | Da | [✓] |

### 10.2 Ce NU Funcționează – Limitări Cunoscute

1. **Limitare 1:** Performanța scade drastic noaptea sau în condiții de vizibilitate foarte redusă (ceață densă), datele de antrenare fiind majoritar de zi.
2. **Limitare 2:** Rezoluția mică (64x64) face dificilă distingerea semnelor aflate la distanță mare în cadru.
3. **Limitare 3:** Ocluziile parțiale (semn acoperit >30%) duc frecvent la erori de clasificare.

### 10.3 Lecții Învățate (Top 5)

1. **[Datele sunt totul]:** Calitatea și diversitatea setului de date (augmentarea) au adus cel mai mare câștig de performanță, mai mult decât tuning-ul fin de hiperparametri.
2. **[Early Stopping]:** Esențială pentru a preveni overfitting-ul și a economisi timp de calcul inutil.
3. **[Arhitectură iterativă]:** Pornirea cu un model simplu și creșterea complexității gradual a permis izolarea problemelor.
4. **[Importanța UI]:** O interfață vizuală bună ajută enorm la debugging-ul modelului ("de ce a prezis asta?").
5. **[State Machine]:** Gândirea în "stări" a făcut aplicația robustă la erori (ex: camera deconectată).

### 10.4 Retrospectivă

**Ce ați schimba dacă ați reîncepe proiectul?**
Aș investi de la început mai mult timp în colectarea unui set de date mai variat (noapte, ploaie), în loc să mă bazez pe augmentări sintetice. De asemenea, aș experimenta cu arhitecturi pre-antrenate (Transfer Learning) încă din fazele timpurii pentru un baseline mai puternic, deși cerința a fost antrenare de la zero.

### 10.5 Direcții de Dezvoltare Ulterioară

| Termen | Îmbunătățire Propusă | Beneficiu Estimat |
|--------|---------------------|-------------------|
| **Short-term** | Colectare date "Night Mode" | +15% acuratețe noaptea |
| **Medium-term** | Portare pe Raspberry Pi + Coral TPU | Sistem embedded portabil |
| **Long-term** | Integrare detecție pietoni | Sistem ADAS complet |

---

## 11. Bibliografie

1. Keras Team, *Keras Documentation*, 2024. URL: https://keras.io/
2. Stallkamp, J. et al., *The German Traffic Sign Recognition Benchmark: A multi-class classification competition*, IJCNN 2011.
3. Géron, A., *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*, O'Reilly Media, 2019.
4. Course Materials, *Rețele Neuronale - Curs & Laborator*, UPB 2025.

---

## 12. Checklist Final (Auto-verificare)

- [x] **Accuracy ≥70%** pe test set (verificat în `results/final_metrics.json`)
- [x] **F1-Score ≥0.65** pe test set
- [x] **Contribuție ≥40% date originale** (verificabil în `data/generated/`)
- [x] **Model antrenat de la zero** (NU pre-trained fine-tuning)
- [x] **Minimum 4 experimente** de optimizare documentate (tabel în Secțiunea 5.3)
- [x] **Confusion matrix** generată și interpretată (Secțiunea 6.2)
- [x] **State Machine** definit cu minimum 4-6 stări (Secțiunea 4.2)
- [x] **Cele 3 module funcționale:** Data Logging, RN, UI (Secțiunea 4.1)
- [x] **Demonstrație end-to-end** disponibilă în `docs/demo/`

### Repository și Documentație

- [x] **README.md** complet (toate secțiunile completate cu date reale)
- [x] **4 README-uri etape** prezente în `docs/` (etapa3, etapa4, etapa5, etapa6)
- [x] **Screenshots** prezente în `docs/screenshots/`
- [x] **Structura repository** conformă cu Secțiunea 8
- [x] **requirements.txt** actualizat și funcțional
- [x] **Cod comentat** (minim 15% linii comentarii relevante)
- [x] **Toate path-urile relative** (nu absolute: `/Users/...` sau `C:\...`)

### Acces și Versionare

- [x] **Repository accesibil** cadrelor didactice RN (public sau privat cu acces)
- [x] **Tag `v0.6-optimized-final`** creat și pushed
- [x] **Commit-uri incrementale** vizibile în `git log` (nu 1 commit gigantic)
- [x] **Fișiere mari** (>100MB) excluse sau în `.gitignore`

### Verificare Anti-Plagiat

- [x] Model antrenat **de la zero** (weights inițializate random, nu descărcate)
- [x] **Minimum 40% date originale** (nu doar subset din dataset public)
- [x] Cod propriu sau clar atribuit (surse citate în Bibliografie)

---

## Note Finale

**Versiune document:** FINAL  
**Data:** 12.02.2026  
**Tag Git:** `v0.6-optimized-final`

---

*Acest README servește ca documentație principală pentru Livrabilul 1 (Aplicație RN). Pentru Livrabilul 2 (Prezentare PowerPoint), consultați structura din RN_Specificatii_proiect.pdf.*
