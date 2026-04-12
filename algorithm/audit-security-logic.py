# Security Audit and Anti-Fraud Logic / Logika audytu i anty-fraud

def initiate_offline_audit(reason_code, session_entropy):
    """
    English: Logs the transition to offline mode to prevent intentional disconnection.
    Polski: Rejestruje przejście w tryb offline, aby zapobiec celowemu odłączaniu sieci.
    """
    audit_entry = {
        "event": "OFFLINE_MODE_START",
        "reason": reason_code,
        "time_oracle": get_trusted_time_priority()[0],
        "entropy": session_entropy # Preventing pre-calculation
    }
    secure_local_log(audit_entry)

def verify_on_sync(local_chain, central_state, terminal_id):
    """
    English: Verifies hash chain continuity upon reconnection for a specific POS terminal.
    Polski: Weryfikuje ciągłość łańcucha hash przy przywróceniu połączenia dla konkretnej kasy.
    """
    # Retrieve the last known hash specific to this physical POS terminal
    expected_base_hash = central_state.get_last_hash_for_terminal(terminal_id)
    
    if not local_chain or len(local_chain) == 0:
        return False
        
    # Check if the local offline chain correctly builds upon the last online state
    if local_chain.first().prev_hash == expected_base_hash:
        return True 
        
    return False
