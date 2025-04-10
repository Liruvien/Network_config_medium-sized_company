Projekt Networkowy: Firmowa infrastruktura sieciowa dla średniej firmy

Wstęp
Celem tego projektu jest stworzenie pełnej infrastruktury sieciowej, która obejmuje konfigurację routerów Cisco, switchy, firewalli pfSense, a także implementację połączenia z chmurą AWS (VPN, VPC). Projekt demonstruje budowę i konfigurację sieci LAN/WAN, polityki bezpieczeństwa oraz zarządzanie DNS, DHCP i routingiem.

Cele projektu
- Zaprojektowanie i skonfigurowanie firmy infrastruktury sieciowej (router, przełączniki, VLAN, VPN i firewall).
- Konfiguracja polityki bezpieczeństwa w firewallu (blokowanie/zezwalanie na ruch).
- Zarządzanie adresacją IP, DHCP i DNS.
- Integracja z chmurą AWS (konfiguracja VPC i VPN site-to-site).
- Monitorowanie i troubleshooting przy użyciu Wireshark.

Narzędzia i Technologie
- **Sprzęt sieciowy:** Cisco (Router c3745), Ethernet Switch, pfSense Firewall.
- **Oprogramowanie:** GNS3, Wireshark.
- **Chmura:** AWS (VPN, VPC).
- **Protokoły:** DHCP, DNS, VLAN, VPN, BGP, OSPF.

Topologia sieci (schemat znajduje się w pliku `network_topology.png`)
- Router Cisco połączony trunkiem ze switchem, który ma skonfigurowane VLANy.
- pfSense Firewall umieszczony pomiędzy routerem a siecią WAN.
- Hosty: Kali Linux, Debian Linux podłączone do switcha.
- Połączenie VPN między pfSense a AWS (site-to-site).

Konfiguracje
- `cisco_router.conf` – konfiguracja routera Cisco (routing, NAT, subinterfejsy dla VLAN).
- `switch.conf` – konfiguracja switcha (VLAN, trunking).
- `pfSense.conf` – opis konfiguracji pfSense (firewall, VPN, DHCP, DNS).

Skrypty i testy
- `backup_config.sh` – skrypt do tworzenia kopii zapasowych konfiguracji routera/switcha.
- `vlan_setup.py` – skrypt automatyzujący konfigurację VLAN na routerze.
- `test_connectivity.py` – skrypt testujący połączenia (ping, traceroute).

Jak uruchomić projekt?
1. Importuj projekt do GNS3 wraz z GNS3 VM.
2. Załaduj konfiguracje urządzeń z plików .conf.
3. Połącz urządzenia zgodnie z diagramem (sprawdź plik `network_topology.png`).
4. Uruchom skrypty testujące i backup.
5. Monitoruj ruch sieciowy przy użyciu Wireshark.

Kable i adresacja
- Użyj następującej liczby kabli:
  - Kabel trunk między routerem a switch.
  - Kabel LAN między switch a pfSense LAN.
  - Kabel łączący pfSense WAN do chm3 NAT lub innego łącza z Internetem.
  - Kabel od switch do hostów (Kali i Debian).
- Przykładowa adresacja:
  - VLAN 10 (HR): 192.168.10.0/24, Router: 192.168.10.1
  - VLAN 20 (IT): 192.168.20.0/24, Router: 192.168.20.1
  - pfSense LAN: 192.168.1.1/24
  - DHCP: zakres 192.168.1.100-192.168.1.200
  - DNS: 192.168.1.2 (może być na pfSense lub osobnym serwerze)

Autor
Klaudia Wojciechowska

