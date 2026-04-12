# T-OTP Protocol: Time-Bound Offline Transaction Protocol
*Cryptographic guarantee of time continuity in untrusted (offline) environments.* *Kryptograficzna gwarancja ciągłości czasu w środowisku niezaufanym (offline).*

---

## 🇬🇧 English Version

Extended Description: The T-OTP Protocol solves the critical vulnerability of untrusted system clocks in distributed points of sale . By anchoring the transaction's "Moment of Freezing" to a GUM-homologated fiscal device, the system creates a cryptographic proof of time that remains valid even if synchronized 24 hours later . This repository serves as a technical blueprint for implementing legally binding offline transactions in accordance with MDR and pharmaceutical regulations .


### Executive Summary
T-OTP is a protocol designed to solve the critical problem of secure timestamping during total network outages in environments handling sensitive goods (pharmacies, medical facilities). 
Unlike standard store-and-forward systems that rely on the PC system clock (which is highly vulnerable to manipulation), T-OTP utilizes sealed hardware modules as a Hardware Oracle. This guarantees the non-repudiation of the exact moment a prescription drug or regulated product was dispensed.

### Patent Status
This technology is legally protected and currently undergoing the patenting process at the **Patent Office of the Republic of Poland (UPRP - [uprp.gov.pl](https://uprp.gov.pl))**.
* **Application Number:** P.454742 (Filed: February 13, 2026)
* **Status:** Patent Pending
* **Core Innovation:** Utilizing fiscal hardware time (GUM homologated) for the validation of non-fiscal authorizations (e-prescriptions).

### The Three Pillars of T-OTP
1. **Hardware Time Oracle:** Retrieving time directly from the sealed RTC (Real-Time Clock) module of a fiscal printer. This is the primary source of trust, completely independent of the PC operating system.
2. **Localchain (Immutable Ledger):** Every offline transaction is mathematically bound to the previous one using a SHA-256 hash function, creating an unbreakable chain.
3. **Hard Lock Controller:** A physical and logical blockade of the printing mechanism until the cryptographic "Frozen Blob" of the transaction is successfully generated.

### Protocol Mechanics
When a network loss is detected (Timeout > 3000ms), the system initiates the "Moment of Freezing" procedure. The core algorithm relies on this mathematical foundation:

$Hash_{TX} = SHA256(Data\_Patient + ID\_Drug + T_{Fiscal} + Hash_{Prev})$

When the internet connection is restored (synchronization up to 24h), the central system (e.g., CROK) can mathematically verify that the drug was dispensed before the prescription expired (e.g., at 23:55), even if the data reaches the server the next morning.

### Repository Contents & Quick Links

**Technical & Algorithmic Implementation:**
* [`algorithm/TOTP_Hybrid.py`](algorithm/TOTP_Hybrid.py) - Core protocol logic and Localchain generation.
* [`algorithm/multi-source-selector.py`](algorithm/multi-source-selector.py) - Fallback logic for redundant time sources.
* [`algorithm/privacy-compliance.py`](algorithm/privacy-compliance.py) - Hybrid PKI encryption for GDPR compliance.
* [`test_totp.py`](test_totp.py) - Automated integrity and anti-tamper verification script.

**Documentation:**
* [`docs/api-documentation-en.md`](docs/api-documentation-en.md) - Full API reference.
* [`docs/mathematical-foundation.md`](docs/mathematical-foundation.md) - Cryptographic formulas and hash logic.
* [`docs/legal-article-4a-proposal.md`](docs/legal-article-4a-proposal.md) - Legislative proposal for offline timestamps.
* [`docs/patent-claims.md`](docs/patent-claims.md) - Core patent claims submitted to UPRP.

### System Visualization
* **FIG. 1: System Architecture** -> [View Diagram](assets/fig1-architecture.png)
* **FIG. 2: T-OTP Flowchart** -> [View Diagram](assets/fig2-flowchart.png)
* **FIG. 3: Data Structure (Localchain)** -> [View Diagram](assets/fig3-data-structure.png)
* **FIG. 4: Hard Lock Mechanism** -> [View Diagram](assets/fig4-hard-lock-logic.png)

---

## 🇵🇱 Wersja Polska

Opis rozszerzony: Protokół T-OTP rozwiązuje krytyczny problem niewiarygodnych zegarów systemowych w rozproszonych punktach sprzedaży . Poprzez zakotwiczenie „Momentu Zamrożenia” transakcji w homologowanym urządzeniu fiskalnym (GUM), system tworzy kryptograficzny dowód czasu, który zachowuje ważność nawet przy synchronizacji z 24-godzinnym opóźnieniem . Repozytorium to służy jako techniczny wzorzec wdrażania prawnie wiążących transakcji offline, zgodnie z MDR i przepisami farmaceutycznymi .

### Podsumowanie (Executive Summary)
T-OTP to protokół rozwiązujący krytyczny problem bezpiecznego znacznika czasu (timestampingu) podczas całkowitych awarii sieci w punktach obrotu towarami wrażliwymi (apteki, placówki medyczne). 
W przeciwieństwie do standardowych systemów store-and-forward, które polegają na zegarze systemowym PC (podatnym na manipulację), T-OTP wykorzystuje zaplombowane moduły sprzętowe jako Hardware Oracle, gwarantując niezaprzeczalność momentu wydania leku.

### Status Patentowy
Technologia jest chroniona prawnie i została zgłoszona w **Urzędzie Patentowym Rzeczypospolitej Polskiej (UPRP - [uprp.gov.pl](https://uprp.gov.pl))**.
* **Numer zgłoszenia:** P.454742 (złożone 13.02.2026)
* **Status:** Patent Pending
* **Innowacja:** Wykorzystanie zaplombowanego czasu fiskalnego (GUM) do walidacji uprawnień pozafiskalnych (e-recepta).

### Trzy Filary T-OTP
1. **Hardware Time Oracle:** Pobieranie czasu z zaplombowanego modułu RTC (Real-Time Clock) drukarki fiskalnej. Jest to źródło nadrzędne i niezależne od systemu operacyjnego.
2. **Localchain (Immutable Ledger):** Każda transakcja offline jest wiązana z poprzednią za pomocą funkcji skrótu SHA-256, tworząc nierozerwalny łańcuch.
3. **Hard Lock Controller:** Fizyczna i logiczna blokada mechanizmu drukującego do momentu poprawnego wygenerowania kryptograficznego zamrożenia transakcji (Frozen Blob).

### Zawartość Repozytorium i Linki

**Implementacja Algorytmiczna:**
* [`algorithm/TOTP_Hybrid.py`](algorithm/TOTP_Hybrid.py) - Główna logika protokołu i generowanie łańcucha Localchain.
* [`algorithm/audit-security-logic.py`](algorithm/audit-security-logic.py) - Zabezpieczenia przeciwko fałszerstwom i atakom typu fork.
* [`algorithm/fail-safe-logic.py`](algorithm/fail-safe-logic.py) - Procedury obsługi awarii sprzętowych (Hardware Fail-Safe).
* [`test_totp.py`](test_totp.py) - Skrypt testowy udowadniający skuteczność wykrywania manipulacji czasem.

**Dokumentacja Prawno-Techniczna:**
* [`docs/api-documentation-pl.md`](docs/api-documentation-pl.md) - Polska dokumentacja techniczna API.
* [`docs/legal-article-4a-proposal.md`](docs/legal-article-4a-proposal.md) - Propozycja legislacyjna uregulowania dowodu czasu offline.
* [`docs/fiscal-printer-integration.md`](docs/fiscal-printer-integration.md) - Szczegóły integracji z urządzeniami fiskalnymi.
* [`docs/patent-claims.md`](docs/patent-claims.md) - Główne zastrzeżenia patentowe P.454742.

### Wizualizacja Systemu
* **FIG. 1: Architektura Systemu** -> [Zobacz Schemat](assets/fig1-architecture.png)
* **FIG. 2: Przepływ Algorytmu T-OTP** -> [Zobacz Schemat](assets/fig2-flowchart.png)
* **FIG. 3: Struktura Danych Localchain** -> [Zobacz Schemat](assets/fig3-data-structure.png)
* **FIG. 4: Logika Blokady Hard Lock** -> [Zobacz Schemat](assets/fig4-hard-lock-logic.png)

---

## Legal Disclaimer and License
**Software:** Udostępniony na licencji MIT. Możesz swobodnie przeglądać i testować kod logiki kryptograficznej.  
**Invention:** Metoda, algorytm i system T-OTP są przedmiotem ochrony własności przemysłowej (zgłoszenie P.454742 w UPRP). Wykorzystanie komercyjne samego protokołu wymaga zgody autora lub licencji patentowej.

## Contact
**Rajo** - Creator of the T-OTP Protocol  
GitHub: [@Rajo-PL](https://github.com/Rajo-PL)
