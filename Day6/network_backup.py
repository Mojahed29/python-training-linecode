import os
from datetime import datetime
from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("SSH_USERNAME")
PASSWORD = os.getenv("SSH_PASSWORD")

devices = [
    {"device_type": "cisco_ios", "ip": "192.168.100.10", "username": USERNAME, "password": PASSWORD},
    {"device_type": "cisco_ios", "ip": "192.168.100.11", "username": USERNAME, "password": PASSWORD},
]

BACKUP_DIR = "./backups"
os.makedirs(BACKUP_DIR, exist_ok=True)

for device in devices:
    ip = device["ip"]
    dev_type = device["device_type"]
    net_connect = None
    print(f"\nAttempting to connect to {ip} ({dev_type})...")

    try:
        net_connect = ConnectHandler(**device)
        hostname = net_connect.send_command("show run | include hostname").split()[-1]
        print(f"Successfully connected to {ip}. Device Hostname: {hostname}")
        
        print(f"Retrieving running configuration from {hostname}...")
        running_config = net_connect.send_command("show running-config")
        
        today = datetime.now().strftime("%Y-%m-%d")
        backup_file = os.path.join(BACKUP_DIR, f"{hostname}_{today}.txt")
        
        with open(backup_file, "w") as f:
            f.write(running_config)
        print(f"Configuration backup for {hostname} saved to {backup_file} successfully.")

    except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
        print(f"Error backing up configuration for {ip}: {e}")

    except Exception as e:
        print(f"An unexpected error occurred for {ip}: {e}")

    finally:
        if net_connect:
            net_connect.disconnect()
            print(f"Disconnected from {ip}.")