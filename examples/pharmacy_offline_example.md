Pharmacy Offline Scenarios / Scenariusze Apteczne Offline
Ten dokument opisuje praktyczne zastosowanie protokołu T-OTP w codziennej pracy apteki. Scenariusze te obrazują, w jaki sposób technologia ta rozwiązuje problemy prawne i techniczne wynikające z braku łączności z systemami centralnymi.

Scenario 1: Standard Offline Dispensing
Scenariusz 1: Standardowe wydanie leku offline
English:
A sudden fiber optic failure occurs at 2:00 PM. The pharmacy loses connection to the P1 system. A patient needs life-saving medication.
Using T-OTP, the pharmacist scans the prescription information printout. The system generates a Frozen Blob using the timestamp from the fiscal printer (Hardware Oracle). A receipt is printed with a unique transaction hash.
Result: The medication is dispensed legally. When the connection is restored at 5:00 PM, the system synchronizes the data. The National Health Fund (NFZ) accepts the transaction because the Moment of Freezing occurred during a documented network outage.

Polski:
O godzinie 14:00 następuje nagła awaria światłowodu. Apteka traci połączenie z systemem P1. Pacjent potrzebuje leku ratującego życie.
Dzięki T-OTP farmaceuta skanuje wydruk informacyjny recepty. System generuje Frozen Blob, korzystając ze znacznika czasu drukarki fiskalnej (Hardware Oracle). Drukowany jest paragon z unikalnym hashem transakcji.
Wynik: Lek zostaje wydany legalnie. Po przywróceniu sieci o 17:00 system synchronizuje dane. NFZ uznaje transakcję, ponieważ Moment Zamrożenia nastąpił w czasie udokumentowanej awarii sieci.

Scenario 2: Saving an Expiring Prescription
Scenariusz 2: Ratowanie recepty wygasającej
English:
It is 11:50 PM. A patient arrives with a prescription that expires at midnight. The central P1 system is down for scheduled maintenance.
If the pharmacist waits for the system to return (e.g., at 1:00 AM), the prescription will be invalid and the pharmacy will lose reimbursement.
T-OTP Solution: At 11:55 PM, the system performs the Moment of Freezing procedure. The fiscal RTC provides an immutable timestamp: 2026-04-13 23:55:12. The transaction is signed with the pharmacy's private key and locked in the Localchain.
Result: Although the data reaches P1 in the morning, the T-OTP timestamp proves the dispensing happened before the expiration. Reimbursement is approved.

Polski:
Jest godzina 23:50. Pacjent zgłasza się z receptą, której ważność kończy się o północy. Centralny system P1 ma przerwę techniczną.
Jeśli farmaceuta poczeka na powrót systemu (np. do 01:00), recepta wygaśnie, a apteka straci refundację.
Rozwiązanie T-OTP: O godzinie 23:55 system wykonuje procedurę Momentu Zamrożenia. Zegar fiskalny dostarcza niezmienny znacznik czasu: 2026-04-13 23:55:12. Transakcja zostaje podpisana kluczem prywatnym apteki i zamknięta w Localchain.
Wynik: Mimo że dane trafiają do P1 rano, znacznik czasu T-OTP udowadnia, że wydanie nastąpiło przed wygaśnięciem recepty. Refundacja zostaje uznana.

Scenario 3: Fraud Detection (Anti-Backdating)
Scenariusz 3: Wykrywanie oszustw (Antydatowanie)
English:
At 8:00 AM, a dishonest employee tries to record a prescription that expired yesterday by changing the Windows system clock.
T-OTP Protection: The system attempts to generate a hash, but the timestamp is pulled directly from the Hardware Oracle (fiscal printer), which is sealed and cannot be modified via PC. Any attempt to manually edit the Localchain file results in a Hash Mismatch because blocks are cryptographically linked.
Result: The system refuses to authorize the offline transaction. The manipulation attempt is logged in the security audit.

Polski:
O godzinie 08:00 rano nieuczciwy pracownik próbuje zarejestrować receptę, która wygasła wczoraj, zmieniając zegar systemowy Windows.
Ochrona T-OTP: System próbuje wygenerować hash, ale znacznik czasu jest pobierany bezpośrednio z Hardware Oracle (drukarki fiskalnej), która jest zaplombowana i niemożliwa do edycji z poziomu PC. Próba ręcznej edycji pliku Localchain kończy się błędem (Hash Mismatch), ponieważ bloki są powiązane kryptograficznie.
Wynik: System odmawia autoryzacji transakcji. Próba manipulacji zostaje zarejestrowana w audycie bezpieczeństwa.
