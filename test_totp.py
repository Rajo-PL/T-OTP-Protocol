import hashlib
import json
import hmac

# T-OTP Integrity & Authenticity Test Script / Skrypt testowy T-OTP
# Based on patent P.454742 / Na podstawie zgloszenia P.454742

# --- SYMULACJA KLUCZY PKI (Public Key Infrastructure) ---
# W rzeczywistości klucz prywatny siedzi bezpiecznie w module HSM / Karcie Farmaceuty
PHARMACY_PRIVATE_KEY = b"SECURE_HSM_PRIVATE_KEY_9982"
PHARMACY_PUBLIC_KEY = b"PUBLIC_KEY_FOR_CROK_VERIFICATION"

def calculate_hash(data, timestamp, prev_hash):
    """
    Krok C: Generowanie hasza transakcji (Localchain Link)
    Hash_TX = SHA256(Data + "|" + T_Fiscal + "|" + Hash_Prev)
    """
    block_content = f"{data}|{timestamp}|{prev_hash}"
    return hashlib.sha256(block_content.encode('utf-8')).hexdigest()

def sign_transaction(tx_hash, private_key):
    """
    Krok D: Podpis Cyfrowy (Pieczęć Apteki)
    Symulacja podpisu asymetrycznego RSA przy użyciu deterministycznego HMAC.
    Dowodzi, że tylko posiadacz klucza prywatnego może zatwierdzić blok.
    """
    return hmac.new(private_key, tx_hash.encode('utf-8'), hashlib.sha256).hexdigest()

def verify_chain(chain):
    """
    Kompleksowa weryfikacja: Integralność (Hash) + Autentyczność (Podpis)
    """
    for i in range(len(chain)):
        current = chain[i]
        
        # 1. Weryfikacja powiązania kryptograficznego (Localchain)
        prev_hash_expected = chain[i-1]['hash'] if i > 0 else "0"
        if current['prev_hash'] != prev_hash_expected:
            return False, i, "Cryptographic link broken (Chain Fork/Break)"
            
        # 2. Weryfikacja Integralności (Próba manipulacji czasem/danymi)
        expected_hash = calculate_hash(current['data'], current['t_fiscal'], current['prev_hash'])
        if current['hash'] != expected_hash:
            return False, i, "Internal data manipulation detected (Hash mismatch)"

        # 3. Weryfikacja Podpisu (Próba przeliczenia łańcucha przez hakera)
        # System weryfikujący (np. CROK) sprawdza, czy podpis pasuje do hasza
        expected_signature = sign_transaction(current['hash'], PHARMACY_PRIVATE_KEY)
        if current['signature'] != expected_signature:
            return False, i, "Invalid Digital Signature! (Chain Recalculation Attack)"
                
    return True, None, "Valid: Chain is integral and signatures are authentic."

def create_block(data, t_fiscal, prev_hash):
    """Funkcja pomocnicza budująca poprawny blok T-OTP (Frozen Blob)"""
    tx_hash = calculate_hash(data, t_fiscal, prev_hash)
    signature = sign_transaction(tx_hash, PHARMACY_PRIVATE_KEY)
    return {
        "data": data,
        "t_fiscal": t_fiscal,
        "prev_hash": prev_hash,
        "hash": tx_hash,
        "signature": signature
    }

# =====================================================================
# --- SCENARIUSZE TESTOWE (AUDYT BEZPIECZEŃSTWA) ---
# =====================================================================

print("--- [FAZA 1] Generowanie poprawnego lancucha T-OTP ---")
chain = []
# Genesis Block (Blok zerowy)
b0 = create_block("GENESIS", "2026-04-13 10:00:00", "0")
chain.append(b0)

# Kolejna transakcja
b1 = create_block("SALE_001_DRUG_X", "2026-04-13 10:05:00", b0['hash'])
chain.append(b1)

is_valid, err_idx, reason = verify_chain(chain)
print(f"Status łańcucha: {'VALID (ZATWIERDZONY)' if is_valid else 'INVALID'}\n")


print("--- [FAZA 2] Atak 1: Proste Antydatowanie (Zmiana daty w pliku) ---")
# Haker zmienia tylko czas w pliku z logami
chain[1]['t_fiscal'] = "2026-04-12 23:59:59" 
is_valid, err_idx, reason = verify_chain(chain)
print(f"WYNIK: {reason}")
print("Wniosek: Atak odparty. Hash nie pasuje do zmanipulowanej daty.\n")


print("--- [FAZA 3] Atak 2: Przeliczenie Łańcucha (Chain Recalculation) ---")
# Haker to programista. Zmienia czas, a następnie przelicza od nowa Hash_TX, 
# aby oszukać weryfikację z Fazy 2.
chain[1]['t_fiscal'] = "2026-04-12 23:59:59"
# Haker sam oblicza nowy, poprawny matematycznie hash dla fałszywej daty
hacker_new_hash = calculate_hash(chain[1]['data'], chain[1]['t_fiscal'], chain[1]['prev_hash'])
chain[1]['hash'] = hacker_new_hash 

# Ponowna weryfikacja przez system rządowy
is_valid, err_idx, reason = verify_chain(chain)
print(f"WYNIK: {reason}")
print("Wniosek: Atak odparty! Haker podrobił Hash, ale nie posiadał klucza prywatnego apteki, aby wygenerować nowy, prawidłowy Podpis Cyfrowy (Signature).")
