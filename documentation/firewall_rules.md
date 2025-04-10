Plik zawiera politykę zarządzania zaporą sieciową.
# Reguły Firewall pfSense

## Podstawowe ustawienia:
- **Interfejs WAN:** Ruch przychodzący z Internetu ma być domyślnie blokowany, z wyjątkiem ruchu VPN.
- **Interfejs LAN:** Domyślnie zezwalać na ruch wychodzący; blokowanie ruchu przychodzącego spoza VPN.

## Przykładowe reguły:

1. **Reguła VPN:**
   - **Source:** Any (lub zdefiniowana sieć zdalna VPN)
   - **Destination:** Any
   - **Service:** IPSec / UDP 500 / UDP 4500
   - **Action:** Allow

2. **Reguła LAN:**
   - Zezwól na cały ruch wychodzący.
   - Blokuj nieautoryzowany ruch przychodzący (domyślnie).

3. **Reguła blokowania:**
   - Blokuj ruch przychodzący z określonych, podejrzanych IP.

*Pamiętaj, aby każda zmiana reguł była dokumentowana i testowana pod kątem wpływu na działanie sieci.*
