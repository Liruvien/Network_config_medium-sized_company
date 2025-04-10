#!/usr/bin/env python3
import paramiko

def send_commands(ip, username, password, commands):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"Łączenie z {ip}...")
    ssh.connect(ip, username=username, password=password)
    shell = ssh.invoke_shell()

    for cmd in commands:
        shell.send(cmd + '\n')
        import time
        time.sleep(1)

    output = shell.recv(65535).decode('utf-8')
    print(output)
    ssh.close()

if __name__ == "__main__":
    router_ip = "192.168.10.1"
    user = "admin"
    pwd = "password"
    vlan_commands = [
        "enable",
        "configure terminal",
        "vlan 30",
        "name SALES",
        "exit",
        "interface GigabitEthernet0/0.30",
        "encapsulation dot1Q 30",
        "ip address 192.168.30.1 255.255.255.0",
        "exit",
        "end",
        "write memory"
    ]
    send_commands(router_ip, user, pwd, vlan_commands)
