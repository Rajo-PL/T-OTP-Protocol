# T-OTP Protocol

**Time-Bound Offline Transaction Protocol**

Secure offline timestamping and transaction registration for regulated products (pharmaceuticals, medical devices, prescriptions).

---

## About

T-OTP is a protocol that solves the problem of **secure transaction timestamping during complete network outages** in pharmacies and other points of sale of regulated goods.

It uses the **sealed Real-Time Clock (RTC) module from a fiscal printer** as a trusted Hardware Oracle, creates an immutable local hash chain (Localchain based on SHA-256), and implements a Hard Lock mechanism to prevent printing a receipt until the transaction is cryptographically secured.

This provides mathematical proof that a product was dispensed at a specific time, even if synchronization with central systems (CROK, ZSMOPL, P1) occurs many hours later.

**Patent Status**  
Patent application filed in Poland: **P.454742** (filed 13 February 2026)

---

## Key Features

- Trusted time source from fiscal printer RTC (GUM-homologated and tamper-resistant)
- Localchain – immutable SHA-256 hash chain preventing retroactive modifications
- Hard Lock Controller – blocks receipt printing until transaction is secured
- Frozen Blob – cryptographically signed offline transaction package
- Asynchronous Store & Forward synchronization
- Non-repudiation of transaction time
- Designed for Business Continuity in critical pharmaceutical systems

---

## How It Works (Simplified)

1. Network outage detected → Offline Mode
2. Retrieve trusted timestamp (`T_Fiscal`) from fiscal printer RTC
3. Generate transaction hash:  
   `SHA256(PatientData + DrugID + T_Fiscal + PreviousHash)`
4. Create digital signature and "Frozen Blob"
5. Print receipt with "TRYB AWARYJNY - OFFLINE" annotation
6. Store securely locally
7. Synchronize when network is restored

---

## Repository Contents

- `algorithm/` – implementation and pseudocode
- `docs/` – detailed description and patent documents
- `examples/` – usage examples

---

## License

This code is released under the **MIT License**.  
However, the core inventive concept and method are protected by the pending Polish patent application **P.454742**.

---

## Contact & Collaboration

 
Creator of T-OTP Protocol  

Email: [Twój email]  
GitHub: @Rajo-PL

---

**Polska wersja / Polish version**

**T-OTP (Time-Bound Offline Transaction Protocol)** – Bezpieczny protokół znacznika czasu i rejestracji transakcji offline dla produktów reglamentowanych (leki, wyroby medyczne, recepty).

Wykorzystuje zaplombowany moduł RTC drukarki fiskalnej jako zaufane źródło czasu, lokalny łańcuch hash (Localchain) oraz mechanizm Hard Lock. Zapewnia niezaprzeczalność czasu transakcji nawet przy braku internetu.

Zgłoszenie patentowe: **P.454742**
