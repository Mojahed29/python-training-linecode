import paramiko
import os

HOST     = "192.168.1.1"  
USERNAME = "testuser"    

key_path = os.path.expanduser("~/.ssh/id_rsa_paramiko")
private_key = paramiko.RSAKey.from_private_key_file(key_path)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(hostname=HOST, username=USERNAME, pkey=private_key)
    print("[+] Connected successfully using SSH key!")

    stdin, stdout, stderr = client.exec_command("hostname && whoami && uptime")
    print("\n--- Command Output ---")
    for line in stdout.readlines():
        print(line.strip())

except Exception as e:
    print(f"[-] Connection failed: {e}")

finally:
    client.close()
    print("\n[+] Connection closed.")