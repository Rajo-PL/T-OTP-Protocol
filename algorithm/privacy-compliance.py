# Privacy and Compliance Logic / Logika ochrony danych i RODO

def seal_frozen_blob(transaction_data, pharmacy_public_key):
    """
    English: Encrypts sensitive data so it's only readable by the central CROK system.
    Polski: Szyfruje dane wrażliwe, aby były czytelne tylko dla centralnego systemu CROK.
   
    """
    encrypted_payload = encrypt(transaction_data, pharmacy_public_key)
    return encrypted_payload # Zero-Knowledge local storage

def purge_after_sync(transaction_id):
    """
    English: Automatically deletes local data after verified central synchronization.
    Polski: Automatycznie usuwa dane lokalne po zweryfikowanej synchronizacji centralnej.
   
    """
    if central_confirm(transaction_id):
        delete_local_encrypted_copy(transaction_id) # Minimizing local footprint
