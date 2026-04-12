Data Privacy and Regulatory Compliance
Ochrona danych i zgodność z przepisami (RODO)

English Version:
T-OTP ensures Compliance by Design for sensitive pharmaceutical data:

1. [cite_start]Frozen Blob Encryption: Patient data and prescription details are encrypted using the pharmacy's public key before being stored in the local "Black Box"[cite: 43, 45, 174, 176].
2. Zero-Knowledge Proof at Local Level: Only the cryptographic hash (Hash_TX) is visible in the local logs, while the actual payload is accessible only to the central CROK system after synchronization.
3. Auto-Purge: Local Encrypted Storage is cleared immediately after a successful, verified synchronization with the central system to minimize the local data footprint.

Wersja Polska:
T-OTP zapewnia zgodność z RODO (Privacy by Design) dla wrażliwych danych farmaceutycznych:

1. [cite_start]Szyfrowanie Frozen Blob: Dane pacjenta i szczegóły recepty są szyfrowane kluczem publicznym apteki przed zapisaniem w lokalnej "Czarnej Skrzynce"[cite: 43, 45, 174, 176].
2. Minimalizacja danych: W lokalnych logach widoczny jest tylko skrót kryptograficzny (Hash_TX), podczas gdy właściwy ładunek danych jest dostępny tylko dla systemu centralnego CROK po synchronizacji.
