#!/usr/bin/env python3
import os

def ping_host(ip):
    print(f"Pingowanie {ip}...")
    response = os.system(f"ping -c 3 {ip}")
    if response == 0:
        print(f"{ip} jest osiągalny")
    else:
        print(f"{ip} nie odpowiada")

if __name__ == "__main__":
    hosts = ["192.168.10.1", "192.168.20.1", "192.168.1.1", "8.8.8.8"]
    for host in hosts:
        ping_host(host)
