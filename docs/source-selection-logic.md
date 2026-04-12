Source Selection Logic
Logika wyboru źródła czasu

English Version:
To ensure maximum reliability, the T-OTP algorithm implements the following sequence for selecting the timestamp source:

Step 1: Initiation of the offline procedure.
Step 2: Attempt communication with the fiscal printer via serial port or LAN. If successful, retrieve T_Fiscal and proceed to hash generation.
Step 3: If the printer does not respond, query the certified temperature recorder (thermometer). If successful, retrieve T_Thermo and mark the source in the metadata.
Step 4: If the thermometer is unavailable, check the status of the GSM/LTE module. Retrieve NITZ time from the operator's network.
Step 5: If none of the above are available, activate the GPS/GNSS receiver and wait for satellite synchronization.
Step 6: After obtaining time from the most reliable available source, close the transaction block in the Localchain and release the Hard Lock.

Information about the used time source is permanently saved in the Frozen Blob structure, allowing the central system to assess the level of trust in a given transaction during later synchronization.

Wersja Polska:
W celu zapewnienia maksymalnej niezawodności, algorytm T-OTP realizuje następującą sekwencję wyboru źródła sygnatury czasowej:

Krok 1: Inicjacja procedury offline.
Krok 2: Próba nawiązania komunikacji z drukarką fiskalną przez port szeregowy lub LAN. Jeśli sukces, pobierz T_Fiscal i przejdź do generowania hasha.
Krok 3: W przypadku braku odpowiedzi drukarki, wyślij zapytanie do certyfikowanego rejestratora temperatury (termometru). Jeśli sukces, pobierz T_Thermo i oznacz źródło w metadanych.
Krok 4: Jeśli termometr jest niedostępny, sprawdź status modułu GSM/LTE. Pobierz czas NITZ z sieci operatora.
Krok 5: W przypadku braku powyższych, aktywuj odbiornik GPS/GNSS i czekaj na synchronizację satelitarną.
Krok 6: Po uzyskaniu czasu z najbardziej wiarygodnego dostępnego źródła, zamknij blok transakcji w Localchain i zwolnij blokadę Hard Lock.

Informacja o użytym źródle czasu jest trwale zapisywana w strukturze Frozen Blob, co pozwala systemowi centralnemu na ocenę poziomu zaufania do danej transakcji podczas późniejszej synchronizacji.
