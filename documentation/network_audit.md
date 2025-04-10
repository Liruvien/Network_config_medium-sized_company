Plik opisuje procedury audytu sieciowego i sprawdzania wydajności urządzeń.
# Procedura Audytu Sieci

## Cele audytu:
- Weryfikacja poprawności konfiguracji routera, switcha i pfSense.
- Sprawdzenie polityk bezpieczeństwa.
- Testowanie wydajności połączeń (ping, traceroute).
- Analiza logów systemowych oraz monitorowanie ruchu sieciowego (Wireshark, SNMP).

## Krok po kroku:
1. **Sprawdzenie konfiguracji:**
   - Przegląd pliku `cisco_router.conf` i `switch.conf`.
   - Weryfikacja ustawień interfejsów, VLANów, routingu oraz NAT.
2. **Testy bezpieczeństwa:**
   - Testowanie reguł firewall pfSense przy pomocy narzędzi typu nmap.
   - Analiza ruchu przez Wireshark.
3. **Testy łączności:**
   - Uruchomienie skryptu `test_connectivity.py`.
   - Sprawdzanie odpowiedzi ping z hostów.
4. **Kopia zapasowa konfiguracji:**
   - Uruchomienie skryptu `backup_config.sh` do tworzenia kopii zapasowych.

## Raport:
- Opisz wyniki testów.
- Zidentyfikuj potencjalne zagrożenia lub błędy.
- Zapisz rekomendacje dla poprawy konfiguracji.
