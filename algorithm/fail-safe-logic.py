import datetime

# Hardware Fail-Safe Logic / Logika awaryjna warstwy sprzętowej

def detect_time_drift(source_a_time_str, source_b_time_str, threshold_sec=60):
    """
    English: Compares two hardware sources to detect manipulation or battery failure.
    Polski: Porównuje dwa źródła sprzętowe w celu wykrycia manipulacji lub awarii baterii.
    """
    try:
        # Parse strings to datetime objects before subtraction
        time_a = datetime.datetime.fromisoformat(source_a_time_str)
        time_b = datetime.datetime.fromisoformat(source_b_time_str)
        
        drift = abs((time_a - time_b).total_seconds())
        
        if drift > threshold_sec:
            # Mark as 'Lower Trust Level' if drift is too high
            return "TRUST_LEVEL_LOW", drift
        return "TRUST_LEVEL_HIGH", drift
        
    except ValueError:
        return "TRUST_LEVEL_ERROR", None

def handle_rtc_error():
    """
    English: Fallback to secondary source if primary RTC fails (e.g., date 1900-01-01).
    Polski: Przełączenie na źródło wtórne przy awarii RTC (np. data 1900-01-01).
    """
    pass
