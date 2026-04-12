import hashlib
import json

# T-OTP Integrity Test Script / Skrypt testowy integralnosci T-OTP
# Based on patent P.454742 / Na podstawie zgloszenia P.454742

def calculate_hash(data, timestamp, prev_hash):
    """
    Standard formula / Wzor standardowy:
    Hash_TX = SHA256(Data + T_Fiscal + Hash_Prev)
    Note: Uses '|' delimiter to prevent hash collisions.
    """
    block_content = f"{data}|{timestamp}|{prev_hash}"
    return hashlib.sha256(block_content.encode('utf-8')).hexdigest()

def verify_chain(chain):
    """
    Verifies the mathematical consistency of the Localchain.
    Weryfikuje matematyczna spojnosc lokalnego lancucha.
    """
    for i in range(len(chain)):
        current = chain[i]
        
        # 1. Internal Integrity: Has the block data been tampered with?
        expected_hash = calculate_hash(current['data'], current['t_fiscal'], current['prev_hash'])
        if current['hash'] != expected_hash:
            return False, i, "Internal block data manipulation detected"

        # 2. External Link: Is it mathematically bound to the previous block?
        if i > 0:
            previous = chain[i-1]
            if current['prev_hash'] != previous['hash']:
                return False, i, "Cryptographic link broken"
                
    return True, None, "Valid"

# --- TEST SCENARIO / SCENARIUSZ TESTOWY ---

print("--- [1] Generating Valid Localchain / Generowanie poprawnego lancucha ---")
chain = []
# Genesis Block
genesis_hash = calculate_hash("GENESIS", "2026-04-13 10:00:00", "0")
chain.append({"data": "GENESIS", "t_fiscal": "2026-04-13 10:00:00", "prev_hash": "0", "hash": genesis_hash})

# Block 2
b2_hash = calculate_hash("SALE_001", "2026-04-13 10:05:00", genesis_hash)
chain.append({"data": "SALE_001", "t_fiscal": "2026-04-13 10:05:00", "prev_hash": genesis_hash, "hash": b2_hash})

is_valid, error_idx, reason = verify_chain(chain)
print(f"Chain status: {'VALID' if is_valid else 'INVALID'}")

print("\n--- [2] Attempting Tampering (Backdating Block 1) / Proba antydatowania ---")
# Manually changing T_Fiscal in the first block
chain[0]['t_fiscal'] = "2026-04-12 23:59:59" 
print(f"Modified Block 1 time to: {chain[0]['t_fiscal']}")

print("\n--- [3] Final Verification / Koncowa weryfikacja ---")
is_valid, error_idx, reason = verify_chain(chain)
if not is_valid:
    print(f"RESULT: Tampering DETECTED at Block {error_idx}!")
    print(f"REASON: {reason}")
else:
    print("RESULT: Failure! Tampering was not detected.")
