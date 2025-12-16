# 📘 README – Etapa 4: Arhitectura Completă a Aplicației SIA bazată pe Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Bălan Ionuț-Valentin
**Link Repository GitHub** https://github.com/AndreiPopescu/TrafficMind
**Data:** 09.12.2025  
---

## Scopul Etapei 4

Această etapă corespunde punctului **5. Dezvoltarea arhitecturii aplicației software bazată pe RN** din lista de 9 etape - slide 2 **RN Specificatii proiect.pdf**.

**Trebuie să livrați un SCHELET COMPLET și FUNCȚIONAL al întregului Sistem cu Inteligență Artificială (SIA). In acest stadiu modelul RN este doar definit și compilat (fără antrenare serioasă).**

### IMPORTANT - Ce înseamnă "schelet funcțional":

 **CE TREBUIE SĂ FUNCȚIONEZE:**
- Toate modulele pornesc fără erori
- Pipeline-ul complet rulează end-to-end (de la date → până la output UI)
- Modelul RN este definit și compilat (arhitectura există)
- Web Service/UI primește input și returnează output

 **CE NU E NECESAR ÎN ETAPA 4:**
- Model RN antrenat cu performanță bună
- Hiperparametri optimizați
- Acuratețe mare pe test set
- Web Service/UI cu funcționalități avansate

**Scopul anti-plagiat:** Nu puteți copia un notebook + model pre-antrenat de pe internet, pentru că modelul vostru este NEANTRENAT în această etapă. Demonstrați că înțelegeți arhitectura și că ați construit sistemul de la zero.

---

##  Livrabile Obligatorii

### 1. Tabelul Nevoie Reală → Soluție SIA → Modul Software (max ½ pagină)
Completați in acest readme tabelul următor cu **minimum 2-3 rânduri** care leagă nevoia identificată în Etapa 1-2 cu modulele software pe care le construiți (metrici măsurabile obligatoriu):

| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul vostru** | **Modul software responsabil** |
|---------------------------|--------------------------------|--------------------------------|
| Asistență șofer pentru identificarea semnelor de circulație | Detecție și clasificare în timp real (< 100ms/frame) cu afișare pe HUD/Ecran | Neural Network + Camera App |
| Reducerea accidentelor prin avertizare la semne critice (Stop, Sens Interzis) | Alertă vizuală accentuată (Roșu/Verde) în funcție de încredere (> 70%) | Camera App Logic + Inference |
| Colectarea de date din trafic real pentru îmbunătățire continuă | Modul de achiziție imagini cu etichetare automată/manuală | Data Acquisition Module |

**Instrucțiuni:**
- Fiți concreti (nu vagi): "detectare fisuri sudură" ✓, "îmbunătățire proces" ✗
- Specificați metrici măsurabile: "< 2 secunde", "> 95% acuratețe", "reducere 20%"
- Legați fiecare nevoie de modulele software pe care le dezvoltați

---

### 2. Contribuția Voastră Originală la Setul de Date – MINIM 40% din Totalul Observațiilor Finale

**Regula generală:** Din totalul de **N observații finale** în `data/processed/`, **minimum 40%** trebuie să fie **contribuția voastră originală**.

#### Cum se calculează 40%:

**Exemplu 1 - Dataset DOAR public în Etapa 3:**
```
Etapa 3: Ați folosit 10,000 samples dintr-o sursa externa (ex: Kaggle)
Etapa 4: Trebuie să generați/achiziționați date astfel încât:
  
Opțiune A: Adăugați 6,666 samples noi → Total 16,666 (6,666/16,666 = 40%)
Opțiune B: Păstrați 6,000 publice + 4,000 generate → Total 10,000 (4,000/10,000 = 40%)
```

**Exemplu 2 - Dataset parțial original în Etapa 3:**
```
Etapa 3: Ați avut deja 3,000 samples generate + 7,000 publice = 10,000 total
Etapa 4: 3,000 samples existente numără ca "originale"
        Dacă 3,000/10,000 = 30% < 40% → trebuie să generați încă ~1,700 samples
        pentru a ajunge la 4,700/10,000 = 47% > 40% ✓
```

**Exemplu 3 - Dataset complet original:**
```
Etapa 3-4: Generați toate datele (simulare, senzori proprii, etichetare manuală - varianta recomandata)
           → 100% original ✓ (depășește cu mult 40% - FOARTE BINE!)
```

#### Tipuri de contribuții acceptate (exemple din inginerie):

Alegeți UNA sau MAI MULTE dintre variantele de mai jos și **demonstrați clar în repository**:

| **Tip contribuție** | **Exemple concrete din inginerie** | **Dovada minimă cerută** |
|---------------------|-------------------------------------|--------------------------|
| **Date generate prin simulare fizică** | • Traiectorii robot în Gazebo• Vibrații motor cu zgomot aleator calibrat• Consumuri energetice proces industrial simulat | Cod Python/LabVIEW funcțional + grafice comparative (simulat vs real din literatură) + justificare parametri |
| **Date achiziționate cu senzori proprii** | • 500-2000 măsurători accelerometru pe motor• 100-1000 imagini capturate cu cameră montată pe robot• 200-1000 semnale GPS/IMU de pe platformă mobilă• Temperaturi/presiuni procesate din Arduino/ESP32 | Foto setup experimental + CSV-uri produse + descriere protocol achiziție (frecvență, durata, condiții) |
| **Etichetare/adnotare manuală** | • Etichetat manual 1000+ imagini defecte sudură• Anotat 500+ secvențe video cu comportamente robot• Clasificat manual 2000+ semnale vibrații (normal/anomalie)• Marcat manual 1500+ puncte de interes în planuri tehnice | Fișier Excel/JSON cu labels + capturi ecran tool etichetare + log timestamp-uri lucru |
| **Date sintetice prin metode avansate** | • Simulări FEM/CFD pentru date dinamice proces | Cod implementare metodă + exemple before/after + justificare hiperparametri + validare pe subset real |

#### Declarație obligatorie în README:

Scrieți clar în acest README (Secțiunea 2):

```markdown
### Contribuția originală la setul de date:

**Total observații finale:** [N] (după Etapa 3 + Etapa 4)
**Observații originale:** [M] (40% planificat)

**Tipul contribuției:**
[ ] Date generate prin simulare fizică  
[x] Date achiziționate cu senzori proprii  
[x] Etichetare/adnotare manuală  
[ ] Date sintetice prin metode avansate  

**Descriere detaliată:**
Pentru a asigura robustețea modelului în condiții reale de trafic din România, vom completa setul de date public (Kaggle) cu imagini proprii.
Aceste imagini vor fi achiziționate folosind telefonul mobil în scenarii diverse de iluminare și unghiuri.
Imaginile vor fi adnotate manual (bounding box + clasă) pentru a corespunde formatului de intrare al rețelei.

**Locația codului:** `src/data_acquisition/capture.py`
**Locația datelor:** `data/images/`
```

#### Exemple pentru "contribuție originală":
-Simulări fizice realiste cu ecuații și parametri justificați  
-Date reale achiziționate cu senzori proprii (setup documentat)  
-Augmentări avansate cu justificare fizică (ex: simulare perspective camera industrială)  


#### Atenție - Ce NU este considerat "contribuție originală":

- Augmentări simple (rotații, flips, crop) pe date publice  
- Aplicare filtre standard (Gaussian blur, contrast) pe imagini publice  
- Normalizare/standardizare (aceasta e preprocesare, nu generare)  
- Subset dintr-un dataset public (ex: selectat 40% din ImageNet)


---

### 3. Diagrama State Machine a Întregului Sistem (OBLIGATORIE)

**Cerințe:**
- **Minimum 4-6 stări clare** cu tranziții între ele
- **Formate acceptate:** PNG/SVG, pptx, draw.io 
- **Locație:** `docs/state_machine.*` (orice extensie)
- **Legendă obligatorie:** 1-2 paragrafe în acest README: "De ce ați ales acest State Machine pentru nevoia voastră?"

**Stări tipice pentru un SIA:**
```
IDLE → ACQUIRE_DATA → PREPROCESS → INFERENCE → DISPLAY/ACT → LOG → [ERROR] → STOP
                ↑______________________________________________|
```

**Legendă obligatorie (scrieți în README):**
```markdown
### Justificarea State Machine-ului ales:

Am ales arhitectura de tip **monitorizare continuă (real-time loop)** pentru că proiectul vizează asistența șoferului, unde latența mică și feedback-ul vizual continuu sunt critice.

Stările principale implementate în `camera_app.py` sunt:
1. **INIT_MODEL**: Încărcarea modelului neuronal compilat (.h5) și verificarea existenței acestuia.
2. **INIT_CAMERA**: Deschiderea fluxului video de la camera web și setarea rezoluției (1280x720).
3. **CAPTURE_FRAME**: Citirea ciclică a cadrelor video (Frame-by-Frame).
4. **ROI_EXTRACTION**: Extragerea regiunii de interes (centrul imaginii) pentru procesare.
5. **PREPROCESS**: Redimensionare la 64x64, normalizare, expandare dimensiuni pentru intrarea în CNN.
6. **INFERENCE**: Rularea modelului `model.predict()` pentru a obține scorurile de încredere.
7. **DISPLAY**: Afișarea rezultatului (Label + Confidence) și a bounding box-ului pe imaginea originală (Verde dacă >70%, Roșu altfel).

Tranzițiile critice sunt:
- **CAPTURE_FRAME** → **PREPROCESS**: Se execută doar dacă citirea cadrului este validă.
- **INFERENCE** → **DISPLAY**: Se execută instantaneu pentru a menține un FPS ridicat.
- **Validare Scor**: Dacă `confidence > 70%`, se afișează clasa; altfel, "Not found".

Această arhitectură asigură un feedback vizual rapid și gestionează erorile de citire a camerei prin ieșirea controlată din buclă.
```

---

### 4. Scheletul Complet al celor 3 Module Cerute la Curs (slide 7)

Toate cele 3 module trebuie să **pornească și să ruleze fără erori** la predare. Nu trebuie să fie perfecte, dar trebuie să demonstreze că înțelegeți arhitectura.

| **Modul** | **Python (exemple tehnologii)** | **LabVIEW** | **Cerință minimă funcțională (la predare)** |
|-----------|----------------------------------|-------------|----------------------------------------------|
| **1. Data Logging / Acquisition** | `src/data_acquisition/` | LLB cu VI-uri de generare/achiziție | **MUST:** Produce CSV cu datele voastre (inclusiv cele 40% originale). Cod rulează fără erori și generează minimum 100 samples demonstrative. |
| **2. Neural Network Module** | `src/neural_network/model.py` sau folder dedicat | LLB cu VI-uri RN | **MUST:** Modelul RN definit, compilat, poate fi încărcat. **NOT required:** Model antrenat cu performanță bună (poate avea weights random/inițializați). |
| **3. Web Service / UI** | Streamlit, Gradio, FastAPI, Flask, Dash | WebVI sau Web Publishing Tool | **MUST:** Primește input de la user și afișează un output. **NOT required:** UI frumos, funcționalități avansate. |

#### Detalii per modul:

#### **Modul 1: Data Logging / Acquisition**

**Funcționalități obligatorii:**
- [x] Cod rulează fără erori: `python src/data_acquisition/generate.py` sau echivalent LabVIEW
- [x] Generează CSV în format compatibil cu preprocesarea din Etapa 3
- [x] Include minimum 40% date originale în dataset-ul final
- [x] Documentație în cod: ce date generează, cu ce parametri

#### **Modul 2: Neural Network Module**

**Funcționalități obligatorii:**
- [x] Arhitectură RN definită și compilată fără erori (`src/neural_network/train_model.py`)
- [x] Model poate fi salvat și reîncărcat (`traffic_sign_model.h5`)
- [x] Include justificare pentru arhitectura aleasă (CNN cu 3 blocuri convoluționale)
- [x] **NU trebuie antrenat** cu performanță bună (weights pot fi random)


#### **Modul 3: Web Service / UI**

**Funcționalități MINIME obligatorii:**
- [x] Propunere Interfață ce primește input de la user (Feed Camera Web) (`src/neural_network/camera_app.py`)
- [x] Includeți un screenshot demonstrativ în `docs/screenshots/`
- [x] UI pornește și afișează fluxul video cu inferență

**Ce NU e necesar în Etapa 4:**
- UI frumos/profesionist cu grafică avansată
- Funcționalități multiple (istorice, comparații, statistici)
- Predicții corecte (modelul e neantrenat, e normal să fie incorect)
- Deployment în cloud sau server de producție

**Scop:** Prima demonstrație că pipeline-ul end-to-end funcționează: input user → preprocess → model → output.


## Structura Repository-ului la Finalul Etapei 4 (OBLIGATORIE)

**Verificare consistență cu Etapa 3:**

```
proiect-rn-[nume-prenume]/
├── data/
│   ├── raw/
│   ├── processed/
│   ├── generated/  # Date originale
│   ├── train/
│   ├── validation/
│   └── test/
├── src/
│   ├── data_acquisition/
│   ├── preprocessing/  # Din Etapa 3
│   ├── neural_network/
│   └── app/  # UI schelet
├── docs/
│   ├── state_machine.*           #(state_machine.png sau state_machine.pptx sau state_machine.drawio)
│   └── [alte dovezi]
├── models/  # Untrained model
├── config/
├── README.md
├── README_Etapa3.md              # (deja existent)
├── README_Etapa4_Arhitectura_SIA.md              # ← acest fișier completat (în rădăcină)
└── requirements.txt  # Sau .lvproj
```

**Diferențe față de Etapa 3:**
- Adăugat `data/generated/` pentru contribuția dvs originală
- Adăugat `src/data_acquisition/` - MODUL 1
- Adăugat `src/neural_network/` - MODUL 2
- Adăugat `src/app/` - MODUL 3
- Adăugat `models/` pentru model neantrenat
- Adăugat `docs/state_machine.png` - OBLIGATORIU
- Adăugat `docs/screenshots/` pentru demonstrație UI

---

## Checklist Final – Bifați Totul Înainte de Predare

### Documentație și Structură
- [x] Tabelul Nevoie → Soluție → Modul complet (minimum 2 rânduri cu exemple concrete completate in README_Etapa4_Arhitectura_SIA.md)
- [x] Declarație contribuție 40% date originale completată în README_Etapa4_Arhitectura_SIA.md
- [x] Cod generare/achiziție date funcțional și documentat
- [x] Dovezi contribuție originală: grafice + log + statistici în `docs/`
- [x] Diagrama State Machine creată și salvată în `docs/state_machine.*`
- [x] Legendă State Machine scrisă în README_Etapa4_Arhitectura_SIA.md (minimum 1-2 paragrafe cu justificare)
- [x] Repository structurat conform modelului de mai sus (verificat consistență cu Etapa 3)

### Modul 1: Data Logging / Acquisition
- [x] Cod rulează fără erori (`python src/data_acquisition/capture.py`)
- [x] Produce minimum 40% date originale din dataset-ul final
- [x] CSV/Format generat compatibil cu preprocesarea din Etapa 3
- [x] Documentație în `src/data_acquisition/README.md` cu:
  - [x] Metodă de generare/achiziție explicată
  - [x] Parametri folosiți (frecvență, durată, zgomot, etc.)
  - [x] Justificare relevanță date pentru problema voastră
- [x] Fișiere în `data/generated/` conform structurii

### Modul 2: Neural Network
- [x] Arhitectură RN definită și documentată în cod (docstring detaliat) - versiunea inițială 
- [x] README în `src/neural_network/` cu detalii arhitectură curentă

### Modul 3: Web Service / UI
- [x] Propunere Interfață ce pornește fără erori
- [x] Screenshot demonstrativ în `docs/screenshots/ui_demo.png`
- [x] README în `src/app/` cu instrucțiuni lansare (comenzi exacte)

---

**Predarea se face prin commit pe GitHub cu mesajul:**  
`"Etapa 4 completă - Arhitectură SIA funcțională"`

**Tag obligatoriu:**  
`git tag -a v0.4-architecture -m "Etapa 4 - Skeleton complet SIA"`
