{
  "terminal_id": "POS-01-WAW",
  "t_fiscal": "2026-04-13 23:55:12",
  "data": {
    "presc_id": "1.2.616.454742.example",
    "drug_code": "5909990001234",
    "patient_pesel": "800101XXXXX"
  },
  "prev_hash": "a7b8c9d0e1f2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8",
  "hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "signature": "rsa_signature_sample_8d2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7"
}

T-OTP Data Structure (Frozen Blob) / Struktura danych T-OTP (Zamrożona Paczka)
English:
This file presents a sample JSON structure for a single transaction block. This data format is used to store evidence of an offline transaction in the local Black Box. Each field is critical for the subsequent verification by central authorities.

Polski:
Ten plik prezentuje przykładową strukturę JSON dla pojedynczego bloku transakcji. Ten format danych służy do przechowywania dowodów transakcji offline w lokalnej Czarnej Skrzynce. Każde pole jest kluczowe dla późniejszej weryfikacji przez organy centralne.

Field Definitions / Definicje pól
English:

terminal_id: Unique identifier of the pharmacy POS terminal.

t_fiscal: Trusted timestamp obtained from the Hardware Oracle (fiscal printer).

data: Encrypted or plaintext transaction details (prescription and drug ID).

prev_hash: SHA-256 link to the previous transaction in the Localchain.

hash: Cryptographic fingerprint of the current block content.

signature: Digital seal of the pharmacy, ensuring non-repudiation.

Polski:

terminal_id: Unikalny identyfikator terminala POS w aptece.

t_fiscal: Zaufany znacznik czasu pobrany z Hardware Oracle (drukarki fiskalnej).

data: Zaszyfrowane lub jawne szczegóły transakcji (ID recepty i leku).

prev_hash: Łącznik SHA-256 z poprzednią transakcją w Localchain.

hash: Kryptograficzny odcisk palca zawartości bieżącego bloku.

signature: Cyfrowa pieczęć apteki, zapewniająca niezaprzeczalność.
