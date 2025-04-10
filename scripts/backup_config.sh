#!/bin/bash
# Użytkownik musi podać IP, login, hasło, a konfiguracja zostanie zapisana lokalnie

ROUTER_IP="192.168.10.1"
USER="admin"
BACKUP_DIR="./backups"
DATE=$(date +%Y%m%d_%H%M)

mkdir -p ${BACKUP_DIR}

echo "Backup konfiguracji routera ${ROUTER_IP}..."
ssh ${USER}@${ROUTER_IP} 'show running-config' > ${BACKUP_DIR}/router_config_${DATE}.txt

echo "Backup ukończony."
