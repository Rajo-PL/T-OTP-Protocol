T-OTP Technical API Documentation (English Version)

1. Hardware Oracle: Fiscal Printer Integration (Priority 1)
Integration with a fiscal printer as the primary source of trust.

get_fiscal_rtc_time()
Retrieves the secure TFiscal timestamp directly from the sealed RTC module of the fiscal printer. It bypasses the unreliable PC system clock to ensure legal non-repudiation.
Returns: A unique string containing Date + Time + Fiscal Event Number.

control_hard_lock(status)
Manages the Hard Lock state of the printing mechanism. If status is True, the printer is blocked until a valid T-OTP cryptographic signature is generated for the offline transaction.

2. Core Protocol: TOTPProtocol Class
Main class managing the lifecycle of offline transactions.

create_transaction(patient_id, drug_id, quantity)
Initiates a new transaction in the Moment of Freezing mode.
Parameters: patient_id, drug_id (QR code), quantity.
Returns: frozen_blob - a signed data package with a TFiscal timestamp.

verify_integrity()
Verifies the mathematical consistency of the Localchain. It recalculates SHA-256 hashes for every block and validates the link to the previous record.
Hash formula: Hash_TX = SHA256(Data + TFiscal + Hash_Prev)

3. Time Selection: Multi-Source Selector
Management of redundant time sources (Hardware Oracles).

get_trusted_time_priority()
Retrieves time from the most reliable available source according to the hierarchy:
- Fiscal RTC: Fiscal printer (Highest Priority).
- Thermo RTC: Certified pharmacy thermometer.
- GSM NITZ: Mobile network operator time.
- GPS/GNSS: Precision satellite time.

4. Security and Audit: Audit Logic
Mechanisms preventing abuse in offline mode.

initiate_offline_audit(reason_code)
Records the system transition to offline mode. Logs the reason (e.g., server timeout > 3000ms) and injects entropy from the last online session.

5. Fail-Safe and Privacy
Hardware reliability and GDPR compliance.

detect_time_drift(source_a, source_b)
Compares two independent hardware sources to detect anomalies or RTC battery failure.

seal_frozen_blob(transaction_data, public_key)
Encrypts sensitive data (prescriptions, patients) before saving to the local Black Box.

purge_after_sync(transaction_id)
Automatically deletes local data after receiving synchronization confirmation from the central system.
