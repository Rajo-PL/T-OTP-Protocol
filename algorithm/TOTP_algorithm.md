# Algorytm T-OTP / T-OTP Algorithm

## Krok po kroku / Step by Step

**Krok A – Inicjacja (Hard Lock Bypass)**  
Farmaceuta skanuje kod leku i recepty → wykrycie braku sieci → tryb offline.

**Step A – Initiation**  
Pharmacist scans drug and prescription code → network loss detected → offline mode.

**Krok B – Pobranie czasu fiskalnego**  
Zapytanie do drukarki fiskalnej → otrzymanie `T_Fiscal`.

**Step B – Fiscal Time Retrieval**  
Query to fiscal printer → receive `T_Fiscal`.

**Krok C – Generowanie hasha**  
```python
Hash_TX = SHA256(DanePacjenta + IDLeku + T_Fiscal + Hash_Poprzedniej)
