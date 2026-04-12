# Security Audit and Anti-Fraud Logic / Logika audytu i anty-fraud

def initiate_offline_audit(reason_code):
    """
    English: Logs the transition to offline mode to prevent intentional disconnection.
    Polski: Rejestruje przejście w tryb offline, aby zapobiec celowemu odłączaniu sieci.
   
    """
    audit_entry = {
        "event": "OFFLINE_MODE_START",
        "reason": reason_code,
        "time_oracle": get_trusted_time_priority(),
        "entropy": last_sync_session_id # Preventing pre-calculation
    }
    secure_local_log(audit_entry)

def verify_on_sync(local_chain, central_state):
    """
    English: Verifies hash chain continuity upon reconnection.
    Polski: Weryfikuje ciągłość łańcucha hash przy przywróceniu połączenia.
   
    """
    if local_chain.first().prev_hash == central_state.last_hash:
        return True #
    return False
