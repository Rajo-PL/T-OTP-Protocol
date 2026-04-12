import hashlib
import json
from datetime import datetime

class TOTPProtocol:
    """
    Implementacja Protokołu T-OTP (Time-Bound Offline Transaction Protocol).
    Zabezpiecza transakcje offline poprzez wiązanie ich z czasem fiskalnym (RTC).
    """

    def __init__(self):
        # Lokalny łańcuch transakcji (Localchain)
        self.chain = []
        # Hash pierwszej transakcji (Genesis Hash)
        self.genesis_hash = "0" * 64

    def _get_fiscal_time(self):
        """
        Symulacja pobrania czasu z zaplombowanego modułu RTC drukarki fiskalnej.
        W rzeczywistym systemie: wywołanie sterownika urządzenia (np. protokół Thermal).
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _calculate_hash(self, data, t_fiscal, prev_hash):
        """
        Oblicza hash transakcji zgodnie ze wzorem:
        Hash_TX = SHA256(Data + T_Fiscal + Prev_Hash)
        """
        payload = f"{json.dumps(data)}{t_fiscal}{prev_hash}"
        return hashlib.sha256(payload.encode()).hexdigest()

    def create_transaction(self, patient_id, drug_id, quantity):
        """
        Tworzy nową transakcję w trybie offline (Frozen Blob).
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
        Weryfikuje spójność całego lokalnego łańcucha.
        """
        for i in range(len(self.chain)):
            current = self.chain[i]
            prev_hash_expected = self.chain[i-1]['hash'] if i > 0 else self.genesis_hash
            
            # Sprawdzenie powiązania z poprzednikiem
            if current['prev_hash'] != prev_hash_expected:
                return False, f"Błąd spójności w bloku {i}: Naruszony łańcuch (Localchain Break)!"
            
            # Rekalkulacja hasha dla sprawdzenia manipulacji danymi
            recalc = self._calculate_hash(current['data'], current['t_fiscal'], current['prev_hash'])
            if current['hash'] != recalc:
                return False, f"Błąd spójności w bloku {i}: Wykryto manipulację danymi (Data Tampering)!"
                
        return True, "Łańcuch transakcji jest spójny i nienaruszony."

# --- DEMONSTRACJA DZIAŁANIA ---
if __name__ == "__main__":
    system = TOTPProtocol()
    
    print("--- Inicjacja transakcji offline ---")
    tx1 = system.create_transaction("P-100", "Lek-A", 2)
    print(f"Dodano transakcję 1 (Hash: {tx1['hash'][:16]}...)")
    
    tx2 = system.create_transaction("P-200", "Lek-B", 1)
    print(f"Dodano transakcję 2 (Hash: {tx2['hash'][:16]}...)")
    
    valid, msg = system.verify_integrity()
    print(f"\nStatus weryfikacji: {msg}")
