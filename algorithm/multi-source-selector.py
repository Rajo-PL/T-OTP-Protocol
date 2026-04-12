# Multi-Source Time Selection Logic / Logika wyboru źródła czasu

def get_trusted_time_priority():
    """
    English: Implements a hierarchical fallback for Hardware Oracles.
    Polski: Implementuje hierarchiczne przełączanie awaryjne dla Hardware Oracles.
   
    """
    
    # Priority 1: Fiscal Printer RTC (GUM)
    # Priorytet 1: RTC Drukarki Fiskalnej (GUM)
    fiscal_time = hardware_interface.get_fiscal_rtc()
    if fiscal_time and fiscal_time.is_valid():
        return fiscal_time, "SOURCE_FISCAL_RTC" #

    # Priority 2: Certified Thermometer RTC
    # Priorytet 2: RTC Certyfikowanego Termometru
    thermo_time = hardware_interface.get_thermometer_rtc()
    if thermo_time and thermo_time.is_valid():
        return thermo_time, "SOURCE_THERMO_RTC" #

    # Priority 3: GSM Network (NITZ)
    # Priorytet 3: Sieć GSM (NITZ)
    nitz_time = hardware_interface.get_gsm_nitz()
    if nitz_time:
        return nitz_time, "SOURCE_GSM_NITZ" #

    # Priority 4: GNSS / GPS
    # Priorytet 4: Satelity GNSS / GPS
    gps_time = hardware_interface.get_gps_time()
    if gps_time:
        return gps_time, "SOURCE_GPS_GNSS" #

    raise Exception("Critical Error: No trusted time source available.")
