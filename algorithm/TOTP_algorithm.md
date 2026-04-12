T-OTP Algorithm Step-by-Step / Algorytm T-OTP krok po kroku

🇬🇧 English Version

Step A – Initiation (Hard Lock Bypass)
The pharmacist scans the Batch Passport (drug QR) and the Prescription Code. The system detects a network failure (Timeout > 3000ms) and automatically transitions to Offline Mode.

Step B – Fiscal Time Retrieval (Fiscal Binding)
The pharmacy system bypasses the unreliable PC clock and queries the Fiscal Printer for the current "Fiscal Time". The printer returns a unique string: T Fiscal (Date + Time + Unique Fiscal Event Number).

Step C – Cryptographic Hash Generation
The algorithm creates a digital fingerprint of the transaction (Hash_TX) according to the formula:

HashTX = SHA256(PatientData + DrugID + TFiscal + Previous_Transaction_Hash)

Note: Adding the previous transaction hash creates a Local Blockchain (Localchain). If any past record is modified, the entire chain becomes invalid.

Step D – Digital Signature (Pharmacy Seal)
The generated Hash_TX is signed using the Pharmacy's Private Key (stored in a HSM or pharmacist's crypto-card). This creates a "Frozen Blob" containing the encrypted data, fiscal timestamp, and RSA signature.

Step E – Storage (Black Box)
The "Frozen Blob" is saved in an encrypted container on the local disk ("Black Box"). The fiscal printer prints a receipt with the annotation "TRYB AWARYJNY - ZATWIERDZONO OFFLINE" (Emergency Mode - Approved Offline) and a hash fragment as proof for the patient.

🇵🇱 Wersja Polska

Krok A – Inicjacja (Hard Lock Bypass)
Farmaceuta skanuje Paszport Partii (kod QR leku) oraz Kod Recepty. System wykrywa brak łączności sieciowej (Timeout > 3000ms) i przechodzi w Tryb Offline.

Krok B – Pobranie Znacznika Czasu (Fiscal Binding)
System apteczny pomija niewiarygodny zegar komputera PC i wysyła zapytanie do Drukarki Fiskalnej o aktualny "czas fiskalny". Drukarka zwraca unikalny ciąg: T Fiscal (Data + Godzina + Unikalny Numer Zdarzenia Fiskalnego).

Krok C – Generowanie Hasza Transakcji (Szyfrowanie)
Algorytm tworzy cyfrowy odcisk palca transakcji (HashTX) według wzoru:

HashTX = SHA256(DanePacjenta + IDLeku + TFiscal + HashPoprzedniej_Transakcji)

Wyjaśnienie: Dodanie hasza poprzedniej transakcji tworzy Lokalny Łańcuch Bloków (Localchain). Próba zmiany daty wstecz niszczy sumę kontrolną całego łańcucha.

Krok D – Podpis Cyfrowy (Pieczęć Apteki)
Wygenerowany HashTX jest podpisywany Kluczem Prywatnym Apteki (z karty kryptograficznej farmaceuty lub modułu HSM). Powstaje „Zamrożona Paczka” (Frozen Blob) zawierająca zaszyfrowane dane, znacznik czasu T Fiscal oraz podpis RSA.

Krok E – Zapis (Czarna Skrzynka)
Paczka jest zapisywana w szyfrowanym kontenerze na dysku lokalnym („Czarna Skrzynka”). Drukarka fiskalna drukuje paragon z adnotacją „TRYB AWARYJNY - ZATWIERDZONO OFFLINE” oraz skrótem hasza, co stanowi dowód dla pacjenta.
