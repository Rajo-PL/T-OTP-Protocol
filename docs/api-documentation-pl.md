Dokumentacja techniczna API protokołu T-OTP (Wersja Polska)

1. Hardware Oracle: Integracja z drukarką fiskalną (Priorytet 1)
Integracja z drukarką fiskalną jako głównym źródłem zaufania dla protokołu.

get_fiscal_rtc_time()
Pobiera bezpieczny znacznik czasu TFiscal bezpośrednio z zaplombowanego modułu RTC drukarki. Pomija niewiarygodny zegar systemowy komputera PC.
Zwraca: Unikalny ciąg Data + Godzina + Numer Zdarzenia Fiskalnego.

control_hard_lock(status)
Zarządza blokadą Hard Lock mechanizmu drukującego. Status True uniemożliwia wydruk paragonu do momentu wygenerowania podpisu T-OTP.

2. Core Protocol: Klasa TOTPProtocol
Główna klasa zarządzająca cyklem życia transakcji offline.

create_transaction(patient_id, drug_id, quantity)
Tworzy nową transakcję w trybie Momentu Zamrożenia.
Parametry: patient_id, drug_id (paszport partii leku), quantity.
Zwraca: frozen_blob - zaszyfrowany pakiet danych z sygnaturą czasową TFiscal.

verify_integrity()
Weryfikuje matematyczną spójność lokalnego łańcucha Localchain. Rekalkuluje hashe SHA-256 dla każdego bloku i sprawdza powiązania z poprzednikami.

3. Time Selection: Selektor wielu źródeł
Zarządzanie redundancją źródeł czasu Hardware Oracles.

get_trusted_time_priority()
Pobiera czas z najbardziej wiarygodnego dostępnego źródła według hierarchii:
- Fiscal RTC: Drukarka fiskalna (Priorytet najwyższy).
- Thermo RTC: Certyfikowany termometr apteczny.
- GSM NITZ: Czas sieci operatora komórkowego.
- GPS/GNSS: Precyzyjny czas satelitarny.

4. Security and Audit: Logika audytu
Mechanizmy zapobiegające nadużyciom w trybie offline.

initiate_offline_audit(reason_code)
Rejestruje moment przejścia systemu w tryb offline. Loguje kod przyczyny oraz iniekcję entropii z ostatniej sesji.

5. Fail-Safe i Prywatność
Obsługa awarii i zgodność z RODO.

detect_time_drift(source_a, source_b)
Porównuje dwa niezależne źródła sprzętowe w celu wykrycia anomalii lub awarii baterii RTC.

seal_frozen_blob(transaction_data, public_key)
Szyfruje dane wrażliwe (recepty, pacjenci) przed zapisem w lokalnej Czarnej Skrzynce.

purge_after_sync(transaction_id)
Automatyczne usuwanie danych lokalnych po otrzymaniu potwierdzenia synchronizacji z bazy centralnej.
