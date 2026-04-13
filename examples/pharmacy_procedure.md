Operational Procedure: T-OTP Offline Dispensing
Procedura Operacyjna: Wydawanie Offline T-OTP
Purpose / Cel
English:
This procedure describes the steps a pharmacy technician must take when the pharmacy system loses connection to the central P1 system. It ensures that the transaction is legally secured using the T-OTP protocol.

Polski:
Niniejsza procedura opisuje kroki, jakie technik farmaceutyczny musi podjąć w przypadku utraty połączenia systemu aptecznego z systemem centralnym P1. Gwarantuje ona, że transakcja zostanie prawnie zabezpieczona przy użyciu protokołu T-OTP.

Step 1: Outage Detection / Krok 1: Wykrycie awarii
English:
If the system displays a Network Timeout (3000ms+) error or a Offline Mode Active alert, do not restart the router. Continue the transaction in the current emergency session.

Polski:
Jeśli system wyświetli komunikat Network Timeout (3000ms+) lub alert Tryb Offline Aktywny, nie restartuj routera. Kontynuuj transakcję w bieżącej sesji awaryjnej.

Step 2: Data Entry / Krok 2: Wprowadzanie danych
English:
Scan the Prescription Information Printout (QR code) or enter the Patient's PESEL and the 4-digit code manually.
Add the required medications to the sale list as usual.

Polski:
Zeskanuj wydruk informacyjny recepty (kod QR) lub wprowadź ręcznie PESEL pacjenta oraz 4-cyfrowy kod.
Dodaj wymagane leki do listy sprzedaży, tak jak w trybie standardowym.

Step 3: Triggering the Moment of Freezing / Krok 3: Wywołanie Momentu Zamrożenia
English:
Click the button: Approve Offline (T-OTP).
The system will now query the fiscal printer to obtain the Hardware Oracle timestamp. Wait for the Fiscal Binding Confirmation message on the screen.

Polski:
Kliknij przycisk: Zatwierdź Offline (T-OTP).
System wyśle zapytanie do drukarki fiskalnej w celu pobrania znacznika czasu Hardware Oracle. Poczekaj na komunikat Potwierdzenie powiązania fiskalnego na ekranie.

Step 4: Transaction Finalization / Krok 4: Finalizacja transakcji
English:
The fiscal printer will generate a receipt with a hash fragment.
Hand the receipt to the patient. The transaction is now locked in the Localchain and stored in the Black Box.

Polski:
Drukarka fiskalna wygeneruje paragon z fragmentem hasza transakcji.
Wydaj paragon pacjentowi. Transakcja została zamrożona w Localchain i zapisana w Czarnej Skrzynce.

Step 5: Post-Outage Sync / Krok 5: Synchronizacja po awarii
English:
Once the internet connection is restored, the system will show a Pending Offline Transactions notification.
Click: Synchronize All. Do not delete any local files before the green Success status appears.

Polski:
Po przywróceniu połączenia internetowego system wyświetli powiadomienie Oczekujące transakcje offline.
Kliknij: Synchronizuj wszystko. Nie usuwaj żadnych plików lokalnych przed pojawieniem się zielonego statusu Sukces.

Important Note / Ważna uwaga
English:
The T-OTP protocol protects you legally by proving that the sale happened at the exact time shown on the fiscal receipt, regardless of when the data reaches the National Health Fund (NFZ).

Polski:
Protokół T-OTP chroni Cię prawnie, dowodząc, że sprzedaż nastąpiła dokładnie w czasie wskazanym na paragonie fiskalnym, niezależnie od tego, kiedy dane trafią do NFZ.
