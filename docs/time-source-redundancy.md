Time Source Redundancy in T-OTP Protocol
Redundancja źródeł czasu w protokole T-OTP

English Version:
The T-OTP protocol is designed as a hybrid system that can retrieve trusted time from various hardware modules called Hardware Oracles. This ensures business continuity even if the main fiscal printer fails or in medical facilities that do not use such devices.

Priority 1: Fiscal Printer RTC Module
This is the primary time source due to its homologation by the Central Office of Measures and physical security seals. It provides the highest level of legal trust in the Polish system.

Priority 2: Certified Electronic Thermometer
Pharmacies are legally required to monitor medicine temperatures. Modern recorders have their own sealed Real-Time Clock modules. They can serve as an auxiliary time source as their readings are recognized as reliable by pharmaceutical inspections.

Priority 3: GSM Module with NITZ Protocol
Uses time directly from the mobile network operator's infrastructure. This solution is resistant to local NTP server errors and cannot be manipulated by the end user.

Priority 4: GNSS or GPS Satellite Receiver
A dedicated GPS module connected to the terminal provides time with atomic precision. This is ideal for mobile distribution points or in situations of total ground infrastructure paralysis.

Wersja Polska:
Protokół T-OTP został zaprojektowany jako system hybrydowy, który może pobierać zaufany czas z różnych modułów sprzętowych nazywanych Hardware Oracles. Pozwala to na zachowanie ciągłości pracy nawet w przypadku awarii głównej drukarki fiskalnej lub w placówkach medycznych nieposiadających takich urządzeń.

Priorytet 1: Moduł RTC drukarki fiskalnej
Jest to podstawowe źródło czasu ze względu na homologację Głównego Urzędu Miar i fizyczne plomby zabezpieczające. Zapewnia najwyższy poziom zaufania w polskim systemie prawnym.

Priorytet 2: Certyfikowany termometr elektroniczny
Apteki mają obowiązek monitorowania temperatury leków. Nowoczesne rejestratory posiadają własne, zaplombowane zegary RTC. Mogą one pełnić funkcję pomocniczego źródła czasu, ponieważ ich wskazania są uznawane za wiarygodne podczas kontroli inspekcji farmaceutycznej.

Priorytet 3: Moduł GSM z protokołem NITZ
Wykorzystanie czasu bezpośrednio z infrastruktury operatora sieci komórkowej. Jest to rozwiązanie odporne na błędy lokalnych serwerów NTP i niemożliwe do zmanipulowania przez użytkownika końcowego.

Priorytet 4: Odbiornik sygnału satelitarnego GNSS lub GPS
Dedykowany moduł GPS podłączony do terminala dostarcza czas z precyzją atomową. Jest to rozwiązanie idealne dla mobilnych punktów dystrybucji lub w sytuacjach całkowitego paraliżu infrastruktury naziemnej.
