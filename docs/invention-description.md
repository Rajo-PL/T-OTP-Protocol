# Opis Wynalazku / Invention Description

## Dziedzina techniki / Field of the Invention
Wynalazek dotyczy systemów teleinformatycznych służących do nadzoru nad obrotem towarami wrażliwymi, w szczególności kryptograficznej weryfikacji transakcji farmaceutycznych oraz fiskalnych systemów sterowania sprzedażą.

The invention relates to teleinformatics systems for supervision of sensitive goods turnover, in particular cryptographic verification of pharmaceutical transactions and fiscal sales control systems.

## Stan techniki / State of the Art
Obecnie stosowane systemy (m.in. PLMVS, ZSMOPL, P1) działają w modelu synchronicznym. W przypadku awarii sieci sprzedaż jest blokowana lub przechodzi w tryb manualny, który nie gwarantuje integralności danych.

Current systems (e.g. PLMVS, ZSMOPL, P1) operate in a synchronous model. In case of network failure, sales are either blocked or switched to manual mode, which does not guarantee data integrity.

## Istota wynalazku / Essence of the Invention

**Protokół T-OTP (Time-Bound Offline Transaction Protocol)** zapewnia ciągłość sprzedaży produktów reglamentowanych w trybie offline przy jednoczesnym zagwarantowaniu niezaprzeczalności czasu transakcji.

**T-OTP (Time-Bound Offline Transaction Protocol)** ensures continuity of regulated product sales in offline mode while guaranteeing non-repudiation of transaction time.

**Kluczowe elementy / Key Elements:**
1. Zaufane źródło czasu – zaplombowany moduł RTC drukarki fiskalnej (Hardware Oracle)
2. Lokalny łańcuch kryptograficzny (Localchain) oparty na SHA-256
3. Sprzęgłowa blokada fiskalna (Hard Lock)

1. Trusted time source – sealed RTC module of fiscal printer (Hardware Oracle)
2. Local cryptographic hash chain (Localchain) based on SHA-256
3. Fiscal Hard Lock mechanism
