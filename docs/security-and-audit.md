Security Audit and Anti-Fraud Logic
Logika audytu bezpieczeństwa i przeciwdziałania nadużyciom

English Version:
To prevent intentional disconnection (simulating offline mode to bypass real-time checks), the T-OTP protocol implements a mandatory Audit Trail:

1. [cite_start]Network State Logging: Every transition to offline mode is recorded with a reason code and a timestamp from the Hardware Oracle[cite: 32, 163].
2. [cite_start]Challenge-Response on Reconnection: Upon restoring the connection, the central system (CROK) verifies the continuity of the Hash Chain[cite: 50, 181].
3. Entropy Injection: The Hash_TX includes a unique session ID from the last successful online sync to prevent "pre-calculating" offline chains.

Wersja Polska:
Aby zapobiec celowemu odłączaniu sieci (symulowaniu trybu offline w celu obejścia kontroli w czasie rzeczywistym), protokół T-OTP wdraża obowiązkową ścieżkę audytu:

1. [cite_start]Logowanie stanu sieci: Każde przejście w tryb offline jest rejestrowane wraz z kodem przyczyny i znacznikiem czasu z Hardware Oracle[cite: 32, 163].
2. [cite_start]Weryfikacja przy re-koneksji: Po przywróceniu połączenia system centralny (CROK) weryfikuje ciągłość łańcucha Hash Chain[cite: 50, 181].
3. Iniekcja entropii: Hash_TX zawiera unikalny identyfikator sesji z ostatniej poprawnej synchronizacji online, co zapobiega "wstępnemu obliczaniu" łańcuchów offline.
