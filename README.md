T-OTP Protocol: Time-Bound Offline Transaction Protocol

Kryptograficzna gwarancja ciągłości czasu w środowisku niezaufanym (offline).

Executive Summary

T-OTP to protokół rozwiązujący krytyczny problem bezpiecznego znacznika czasu (timestampingu) podczas całkowitych awarii sieci w punktach obrotu towarami wrażliwymi (apteki, placówki medyczne).

W przeciwieństwie do standardowych systemów store-and-forward, które polegają na zegarze systemowym PC (podatnym na manipulację), T-OTP wykorzystuje zaplombowane moduły sprzętowe jako Hardware Oracle, gwarantując niezaprzeczalność momentu wydania leku lub produktu reglamentowanego.

Patent Status

Technologia chroniona zgłoszeniem patentowym w Urzędzie Patentowym RP:
Numer zgłoszenia: P.454742 (złożone 13.02.2026)
Status: Patent Pending
Innowacja: Wykorzystanie czasu fiskalnego (GUM) do walidacji uprawnień pozafiskalnych (e-recepta).

The Three Pillars of T-OTP

Hardware Time Oracle: Pobieranie czasu z zaplombowanego modułu RTC (Real-Time Clock) drukarki fiskalnej. Jest to źródło nadrzędne i niezależne od systemu operacyjnego.

Localchain (Immutable Ledger): Każda transakcja offline jest wiązana z poprzednią za pomocą funkcji skrótu SHA-256, tworząc nierozerwalny łańcuch.

Hard Lock Controller: Fizyczna i logiczna blokada mechanizmu drukującego do momentu poprawnego wygenerowania kryptograficznego zamrożenia transakcji (Frozen Blob).

System Visualization

FIG. 1: System Architecture
10 - Terminal POS, 11 - Drukarka fiskalna z modułem RTC, 12 - Skaner kodów 2D, 13 - Produkt z Paszportem Partii.

FIG. 2: T-OTP Flowchart
Diagram przepływu sterowania ilustrujący sekwencję kroków od detekcji braku sieci po zapis w lokalnym łańcuchu (Localchain).

FIG. 3: Data Structure (Localchain)
Kryptograficzne powiązanie kolejnych pakietów danych transakcyjnych zapewniające integralność w trybie offline.

FIG. 4: Hard Lock Mechanism
Schemat logiczny układu sterowania, gdzie wydruk paragonu zależy od koniunkcji (Bramka AND) sygnałów walidacji.

Protocol Mechanics

W momencie wykrycia braku sieci (Timeout powyżej 3000ms), system inicjuje procedurę Momentu Zamrożenia:

Hash_TX = SHA256(Data_Patient + ID_Drug + T_Fiscal + Hash_Prev)

Dzięki temu, gdy internet powraca (synchronizacja do 24h), system centralny (np. CROK) może matematycznie zweryfikować, że lek został wydany przed wygaśnięciem recepty (np. o 23:55), mimo że dane dotarły na serwer rano.

Repository Contents

algorithm/ – Implementacja w Pythonie (TOTP_hybrid.py) oraz pseudokod.
docs/ – Dokumentacja patentowa, propozycja legislacyjna (Art. 4a) i specyfikacja techniczna.
assets/ – Rysunki techniczne FIG. 1-4 w wysokiej rozdzielczości.

Legal Disclaimer and License

Software: Udostępniony na licencji MIT. Możesz swobodnie przeglądać i testować kod.
Invention: Metoda, algorytm i system T-OTP są przedmiotem ochrony własności przemysłowej (zgłoszenie P.454742). Wykorzystanie komercyjne samego protokołu wymaga zgody autora lub licencji patentowej.

Contact and Collaboration

Rajo
Creator of T-OTP Protocol
Email: [Twój e-mail]
GitHub: @Rajo-PL

Polska wersja (Skrót)

Protokół T-OTP gwarantuje bezpieczeństwo prawne farmaceuty i pacjenta w warunkach awarii infrastruktury e-zdrowia. Dzięki wykorzystaniu drukarki fiskalnej jako cyfrowego notariusza, możliwe jest udowodnienie ważności transakcji w trybie offline, co eliminuje ryzyko odrzucenia recept przez systemy centralne po przywróceniu łączności.
