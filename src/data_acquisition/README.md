# Modul 1: Data Acquisition (Etapa 4)

Acest modul este responsabil pentru completarea setului de date cu imagini orginale (Minim 40%).

### Structura

- `capture.py`: Script interactiv pentru etichetarea și decuparea semnelor de circulație din poze brute.

### Cum să folosești (Pipeline)

1. **Achiziție**: Poze la semne de circulație cu telefonul. La care variaza unghiul, distanța și lumina.
2. **Transfer**: Copiază pozele în folderul:
   `data/raw/phone_uploads/`
   *(Dacă folderul nu există, scriptul îl creează la prima rulare)*
3. **Rulare Labeler**:
   ```bash
   cd src/data_acquisition
   python capture.py
   ```
4. **Etichetare**:
   - Se va deschide o fereastră cu poza.
   - **Desenează** un dreptunghi cu mouse-ul peste semn.
   - Apasă tasta corespunzătoare:
     - `1`: Crosswalk
     - `2`: NoEntry
     - `3`: PriorityRoad
     - `4`: Roundabout
     - `5`: SpeedLimit
     - `6`: Stop
     - `7`: TrafficLight
     - `8`: Yield
   - Decupajul va fi salvat automat în `data/generated/<clasa>/`.
   - Poza originală este mutată în `data/raw/phone_uploads/done`.

### Rezultat

Imaginile generate sunt salvate direct la dimensiunea **64x64**, gata de antrenare.
Acestea se vor regăsi în `data/generated/` și pot fi combinate cu setul de antrenare principal.
