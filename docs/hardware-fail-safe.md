Hardware Fail-Safe Procedures
Procedury awaryjne dla warstwy sprzętowej

English Version:
The protocol accounts for Hardware Oracle failures (e.g., depleted RTC battery or hardware malfunction):

1. Drift Detection: The system compares the Hardware Oracle time with other redundant sources (e.g., thermometer RTC or NITZ).
2. Failure Fallback: If the primary Fiscal RTC returns an error or an invalid date (e.g., 1900-01-01), the Hard Lock remains active until a secondary trusted source (Priority 2 or 3) is validated.
3. Integrity Flag: Transactions signed during a hardware fail-safe event are marked with a "Lower Trust Level" flag for manual review in the central system.

Wersja Polska:
Protokół uwzględnia awarie Hardware Oracle (np. wyczerpanie baterii RTC lub usterka sprzętowa):

1. Wykrywanie dryftu: System porównuje czas Hardware Oracle z innymi redundantnymi źródłami (np. RTC termometru lub NITZ).
2. Przełączanie awaryjne (Fallback): Jeśli główny RTC fiskalny zwróci błąd lub nieprawidłową datę, blokada Hard Lock pozostaje aktywna do czasu walidacji wtórnego zaufanego źródła (Priorytet 2 lub 3).
3. Flaga integralności: Transakcje podpisane podczas awarii sprzętowej są oznaczane flagą "Lower Trust Level" do ręcznej weryfikacji w systemie centralnym.
