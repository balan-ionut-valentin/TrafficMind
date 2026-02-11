# 📘 README – Etapa 3: Analiza și Pregătirea Setului de Date pentru Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Bălan Ionuț-Valentin
**Data:** 25.11.2025 

---

## Introducere

Acest document descrie activitățile realizate în **Etapa 3**, în care se analizează și se preprocesează setul de date necesar proiectului „Rețele Neuronale". Scopul etapei este pregătirea corectă a datelor pentru instruirea modelului RN, respectând bunele practici privind calitatea, consistența și reproductibilitatea datelor.

---

##  1. Structura Repository-ului Github (versiunea Etapei 3)

```
project-name/
├── README.md
├── docs/
│   └── datasets/          # descriere seturi de date, surse, diagrame
│		 ├── annotations/  # fișiere cu date despre imagine
│		 └── images/ 		# imagini pentru prelucrare
├── data/
│   ├── distributie_clase.png # grafic distribuție clase
│   ├── raw/               # date brute
│   ├── processed/         # date curățate și transformate
│   	  ├── train/       # set de instruire
│   	  ├── validation/  # set de validare
│   	  └── test/        # set de testare
├── src/
│   ├── preprocessing/     # funcții pentru preprocesare
│   ├── data_acquisition/  # generare / achiziție date (dacă există)
│   └── neural_network/    # implementarea RN (în etapa următoare)
├── config/                # fișiere de configurare
├── venv/                  # Virtual Environment în Python
│   ├── Lib/        	   
│   	  ├── site-packages/   # dependențele instalate
│   ├── Scripts/  			# scripturi activare Virtual Environment
│   ├── share/     		
│   └── pyenv.cfg/    		# configurație Virtual Environment
└── requirements.txt       # dependențe Python (dacă aplicabil)
```

---

##  2. Descrierea Setului de Date

### 2.1 Sursa datelor

* **Origine:** Kaggle - Road Sign Detection, dataset public
* **Modul de achiziție:** ☐ Senzori reali / ☐ Simulare / ☑ Fișier extern / ☐ Generare programatică
* **Perioada / condițiile colectării:** Noiembrie 2024 - Ianuarie 2025
### 2.2 Caracteristicile dataset-ului

* **Număr total de observații:** 877
* **Număr de caracteristici (features):** Imagine RGB (3 canale) + Coordonate Bounding Box
* **Tipuri de date:** ☐ Numerice / ☐ Categoriale / ☐ Temporale / ☑ Imagini
* **Format fișiere:** ☐ CSV / ☐ TXT / ☐ JSON / ☑ PNG / ☑ XML

### 2.3 Descrierea fiecărei caracteristici

| **Caracteristică** | **Tip** | **Unitate** | **Descriere** | **Domeniu valori** |
|-------------------|---------|-------------|---------------|--------------------|
| R | numeric | - | Intensitatea pixelului pe canalul de culoare Roșu | 0–255 |
| G | numeric | – | Intensitatea pixelului pe canalul de culoare Verde | 0–255 |
| B | numeric | - | Intensitatea pixelului pe canalul de culoare Albsatru | 0–255 |
| Width | numeric | pixeli | Lățimea imaginii de intrare în rețea | 64  |
| Height | numeric | pixeli |Înălțimea imaginii de intrare în rețea | 64  |
| Label | categorial | Clasa semnului de circulație | {Stop, Speed Limit, Crosswalk, Traffic Light} |

---

##  3. Analiza Exploratorie a Datelor (EDA) – Sintetic

### 3.1 Statistici descriptive aplicate

1. Traffic Light
2. Speed Limit
3. Crosswalk
4. Stop

Distribuția claselor: S-a observat un ușor dezechilibru, clasa "Speed Limit" fiind predominantă.
Dimensiuni: Imaginile originale au rezoluții variate, dar semnele de circulație decupate variază între 30x30px și 150x150px.### 3.2 Analiza calității datelor

### 3.2 Analiza calității datelor

* **Detectarea valorilor lipsă** (% pe coloană)
* **Detectarea valorilor inconsistente sau eronate**
* **Identificarea caracteristicilor redundante sau puternic corelate**

### 3.3 Probleme identificate

* [exemplu] Feature X are 8% valori lipsă
* [exemplu] Distribuția feature Y este puternic neuniformă
* [exemplu] Variabilitate ridicată în clase (class imbalance)

---

##  4. Preprocesarea Datelor

### 4.1 Curățarea datelor

 * S-au parcurs fișierele XML și s-au validat corespondențele cu imaginile PNG.
 * S-au extras doar regiunile de interes (ROI) folosind coordonatele xmin, ymin, xmax, ymax.

### 4.2 Transformarea caracteristicilor

 * Decupare (Cropping): Extragerea semnelor din imaginea de ansamblu.
 * Redimensionare: Toate imaginile au fost aduse la dimensiunea standard de 64x64 pixeli.
 * Normalizare: Pixelii au fost păstrați în format 0-255 (urmează scalarea la 0-1 în etapa de antrenare).

### 4.3 Structurarea seturilor de date

Am utilizat metoda Stratified Split pentru a păstra proporția claselor:
 * Train (80%): Folosit pentru antrenarea rețelei.
 * Validation (10%): Folosit pentru ajustarea hiperparametrilor.
 * Test (10%): Folosit pentru evaluarea finală.

### 4.4 Salvarea rezultatelor preprocesării

* Date preprocesate în `data/processed/`
* Seturi train în foldere dedicate

---

##  5. Fișiere Generate în Această Etapă

* `data/raw/` – date brute
* `data/processed/` – date curățate & transformate
* `data/train/`, `data/validation/`, `data/test/` – seturi finale
* `src/preprocessing/` – codul de preprocesare
* `data/README.md` – descrierea dataset-ului

---

##  6. Stare Etapă (de completat de student)

- [ ] Structură repository configurată
- [ ] Dataset analizat (EDA realizată)
- [ ] Date preprocesate
- [ ] Seturi train/val/test generate
- [ ] Documentație actualizată în README + `data/README.md`

---
