import hashlib
import json
from datetime import datetime

class TOTPProtocol:
    """
    EN: Implementation of the T-OTP (Time-Bound Offline Transaction Protocol).
        Secures offline transactions by cryptographically binding them to fiscal time (RTC).
    PL: Implementacja Protokołu T-OTP. Zabezpiecza transakcje offline poprzez 
        wiązanie ich z czasem fiskalnym (RTC) jako Hardware Oracle.
    """

    def __init__(self):
        # Lokalny łańcuch transakcji / Local transaction chain (Localchain)
        self.chain = []
        # Hash pierwszej transakcji / Genesis Hash
        self.genesis_hash = "0" * 64

    def _get_fiscal_time(self):
        """
        EN: Simulates retrieving time from a sealed RTC module of a fiscal printer.
        PL: Symulacja pobrania czasu z zaplombowanego modułu RTC drukarki fiskalnej.
        """
        # In reality, this queries the hardware driver (e.g., Thermal Protocol)
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _calculate_hash(self, data, t_fiscal, prev_hash):
        """
        EN: Calculates transaction hash using deterministic JSON and pipeline delimiters.
        PL: Oblicza hash transakcji z użyciem deterministycznego JSON i separatorów.
        
        Hash_TX = SHA256(Data + "|" + T_Fiscal + "|" + Prev_Hash)
        """
        # SECURITY FIX: sort_keys=True ensures deterministic hashing. 
        # Delimiter '|' prevents hash collision attacks.
        serialized_data = json.dumps(data, sort_keys=True)
        payload = f"{serialized_data}|{t_fiscal}|{prev_hash}"
        return hashlib.sha256(payload.encode('utf-8')).hexdigest()

    def create_transaction(self, patient_id, drug_id, quantity):
        """
        EN: Creates a new offline transaction (Frozen Blob).
        PL: Tworzy nową transakcję w trybie offline (Frozen Blob).
        """
        t_fiscal = self._get_fiscal_time()
        prev_hash = self.chain[-1]['hash'] if self.chain else self.genesis_hash
        
        tx_data = {
            "patient_id": patient_id,
            "drug_id": drug_id,
            "quantity": quantity
        }
        
        tx_hash = self._calculate_hash(tx_data, t_fiscal, prev_hash)
        
        frozen_blob = {
            "data": tx_data,
            "t_fiscal": t_fiscal,
            "prev_hash": prev_hash,
            "hash": tx_hash,
            "status": "OFFLINE_FROZEN"
        }
        
        self.chain.append(frozen_blob)
        return frozen_blob

    def verify_integrity(self):
        """
        EN: Verifies the mathematical consistency of the entire Localchain.
        PL: Weryfikuje matematyczną spójność całego lokalnego łańcucha.
        """
        for i in range(len(self.chain)):
            current = self.chain[i]
            prev_hash_expected = self.chain[i-1]['hash'] if i > 0 else self.genesis_hash
            
            # 1. External link validation / Sprawdzenie powiązania z poprzednikiem
            if current['prev_hash'] != prev_hash_expected:
                return False, f"Block {i} Integrity Error: Broken Link (Localchain Break)!"
            
            # 2. Internal integrity recalculation / Rekalkulacja hasha dla blokady manipulacji
            recalc = self._calculate_hash(current['data'], current['t_fiscal'], current['prev_hash'])
            if current['hash'] != recalc:
                return False, f"Block {i} Integrity Error: Data Tampering Detected!"
                
        return True, "Valid: Localchain is mathematically consistent and untampered. / Łańcuch jest spójny."

# --- DEMONSTRATION ---
if __name__ == "__main__":
    system = TOTPProtocol()
    
    print("--- T-OTP Offline Transaction Initiation / Inicjacja transakcji ---")
    tx1 = system.create_transaction("P-100", "Drug-A", 2)
    print(f"Transaction 1 added (Hash: {tx1['hash'][:16]}...)")
    
    tx2 = system.create_transaction("P-200", "Drug-B", 1)
    print(f"Transaction 2 added (Hash: {tx2['hash'][:16]}...)")
    
    valid, msg = system.verify_integrity()
    print(f"\nVerification Status: {msg}")
