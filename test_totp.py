import hashlib
import json

# T-OTP Integrity Test Script / Skrypt testowy integralnosci T-OTP
# Based on patent P.454742 / Na podstawie zgloszenia P.454742

def calculate_hash(data, timestamp, prev_hash):
    """
    Standard formula / Wzor standardowy:
    Hash_TX = SHA256(Data + T_Fiscal + Hash_Prev)
    """
    block_content = f"{data}{timestamp}{prev_hash}"
    return hashlib.sha256(block_content.encode()).hexdigest()

def verify_chain(chain):
    """
    Verifies the mathematical consistency of the Localchain.
    Weryfikuje matematyczna spojnosc lokalnego lancucha.
    [cite: 48-50]
    """
    # Sprawdzamy każdy blok w łańcuchu, w tym Genesis
    for i in range(len(chain)):
        current = chain[i]
        
        # 1. Weryfikacja integralności samego bloku (Czy ktoś nie zmienił danych?)
        expected_hash = calculate_hash(current['data'], current['t_fiscal'], current['prev_hash'])
        if current['hash'] != expected_hash:
            return False, i, "Internal block data manipulation detected"

        # 2. Weryfikacja powiązania kryptograficznego z poprzednikiem
        if i > 0:
            previous = chain[i-1]
            if current['prev_hash'] != previous['hash']:
                return False, i, "Cryptographic link broken"
                
    return True, None, "Valid"

# --- TEST SCENARIO / SCENARIUSZ TESTOWY ---

# 1. Generate Valid Chain / Generowanie poprawnego lancucha
print("--- [1] Generating Valid Localchain / Generowanie poprawnego lancucha ---")
chain = []
# Genesis Block [cite: 271]
genesis_hash = calculate_hash("GENESIS", "2026-04-13 10:00:00", "0")
chain.append({"data": "GENESIS", "t_fiscal": "2026-04-13 10:00:00", "prev_hash": "0", "hash": genesis_hash})

# Block 2
b2_hash = calculate_hash("SALE_001", "2026-04-13 10:05:00", genesis_hash)
chain.append({"data": "SALE_001", "t_fiscal": "2026-04-13 10:05:00", "prev_hash": genesis_hash, "hash": b2_hash})

is_valid, error_idx, reason = verify_chain(chain)
print(f"Chain status: {'VALID' if is_valid else 'INVALID'}")

# 2. Attempt Tampering (Backdating) / Proba manipulacji (Antydatowanie)
print("\n--- [2] Attempting Tampering (Backdating Block 1) / Proba antydatowania ---")
# Manually changing T_Fiscal in the first block [cite: 9, 28, 194]
chain[0]['t_fiscal'] = "2026-04-12 23:59:59" 
print(f"Modified Block 1 time to: {chain[0]['t_fiscal']}")

# 3. Final Verification / Koncowa weryfikacja
is_valid, error_idx, reason = verify_chain(chain)
if not is_valid:
    print(f"RESULT: Tampering DETECTED at Block {error_idx}!")
    print(f"REASON: {reason}")
else:
    print("RESULT: Failure! Tampering was not detected.")
