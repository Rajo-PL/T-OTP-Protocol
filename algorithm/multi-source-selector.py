# Multi-Source Time Selection Logic / Logika wyboru źródła czasu

def get_trusted_time_priority():
    """
    English: Implements a hierarchical fallback for Hardware Oracles with strict timeouts.
    Polski: Implementuje hierarchiczne przełączanie awaryjne z rygorystycznymi limitami czasu.
    """
    
    # Priority 1: Fiscal Printer RTC (GUM) - Timeout: 0.5s
    try:
        fiscal_time = hardware_interface.get_fiscal_rtc(timeout=0.5)
        if fiscal_time and fiscal_time.is_valid():
            return fiscal_time, "SOURCE_FISCAL_RTC"
    except TimeoutError:
        pass # Proceed to secondary source

    # Priority 2: Certified Thermometer RTC - Timeout: 0.5s
    try:
        thermo_time = hardware_interface.get_thermometer_rtc(timeout=0.5)
        if thermo_time and thermo_time.is_valid():
            return thermo_time, "SOURCE_THERMO_RTC"
    except TimeoutError:
        pass

    # Priority 3: GSM Network (NITZ) - Timeout: 2.0s
    try:
        nitz_time = hardware_interface.get_gsm_nitz(timeout=2.0)
        if nitz_time:
            return nitz_time, "SOURCE_GSM_NITZ"
    except TimeoutError:
        pass

    # Priority 4: GNSS / GPS - Timeout: 5.0s
    try:
        gps_time = hardware_interface.get_gps_time(timeout=5.0)
        if gps_time:
            return gps_time, "SOURCE_GPS_GNSS"
    except TimeoutError:
        pass

    raise Exception("Critical Error: No trusted time source available.")
