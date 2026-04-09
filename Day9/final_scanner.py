import nmap
import sys
import json
import os
import yagmail
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_PATH = os.path.join(BASE_DIR, 'raw_ping_reports', 'scan_results.json')
TARGET_NETWORK = os.getenv('TARGET_NETWORK', '192.168.100.0/24') 

GMAIL_USER = os.getenv('GMAIL_USER')
GMAIL_PASS = os.getenv('GMAIL_PASS')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')

def ping_scan(network):
    print(f"[*] Scanning {network} for live hosts...")
    nm = nmap.PortScanner()
    try:
        nm.scan(hosts=network, arguments='-sn')
    except nmap.PortScannerError as e:
        print(f"Nmap error: {e}")
        sys.exit(1)

    live_hosts = [host for host in nm.all_hosts() if nm[host].state() == 'up']
    for host in live_hosts:
        print(f'[+] Host Found: {host}')
    return live_hosts

def send_email_yag(attachment_path):
    print("[*] Sending report via yagmail...")
    yag = yagmail.SMTP(GMAIL_USER, GMAIL_PASS)
    
    yag.send(
        to=RECEIVER_EMAIL,
        subject='Network Scan Report',
        contents='Automated scan completed. Find the JSON report attached.',
        attachments=attachment_path
    )
    print("[+] Email sent successfully.")

if __name__ == "__main__":
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)

    hosts_found = ping_scan(TARGET_NETWORK)
    result_dict = {'live_hosts': hosts_found, 'total': len(hosts_found)}

    with open(REPORT_PATH, 'w') as json_file:
        json.dump(result_dict, json_file, indent=4)
    print(f"\n[+] Scan results saved to {REPORT_PATH}")

    try:
        send_email_yag(REPORT_PATH)
    except Exception as e:
        print(f"[-] Email failed: {e}")