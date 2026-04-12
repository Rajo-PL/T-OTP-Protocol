# Privacy and Compliance Logic / Logika ochrony danych i RODO

def seal_frozen_blob(transaction_data, crok_public_key, pharmacy_private_key):
    """
    English: Encrypts data for the central system and signs it locally.
    Polski: Szyfruje dane dla systemu centralnego i podpisuje je lokalnie.
    """
    # 1. Encrypt for confidentiality (Only CROK can read this)
    encrypted_payload = encrypt_for_recipient(transaction_data, crok_public_key)
    
    # 2. Sign for authenticity (Proves the pharmacy generated this package)
    signature = sign_data(encrypted_payload, pharmacy_private_key)
    
    frozen_blob = {
        "payload": encrypted_payload,
        "signature": signature
    }
    
    return frozen_blob

def purge_after_sync(transaction_id, central_confirmation):
    """
    English: Automatically deletes local data after verified central synchronization.
    Polski: Automatycznie usuwa dane lokalne po zweryfikowanej synchronizacji centralnej.
    """
    if central_confirmation.is_valid(transaction_id):
        delete_local_encrypted_copy(transaction_id) # Minimizing local footprint
