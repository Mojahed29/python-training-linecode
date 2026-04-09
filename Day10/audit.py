import nmap
from datetime import datetime
from testing_devices import devices

USE_MOCK = True  

if USE_MOCK:
    from mock import mock_scan_ports as scan_ports
    from mock import mock_check_device_config as check_device_config

else:
    from netmiko import ConnectHandler

    def scan_ports(ip):
        nm = nmap.PortScanner()
        nm.scan(ip, '23,80,161')

        telnet = "closed"
        http = "closed"

        if ip in nm.all_hosts():
            tcp_data = nm[ip].get('tcp', {})

            telnet = tcp_data.get(23, {}).get('state', 'closed')
            http = tcp_data.get(80, {}).get('state', 'closed')

        return telnet, http


    def check_device_config(device):
        try:
            connection = ConnectHandler(
                **device,
                timeout=10,
                banner_timeout=10
            )

            config = connection.send_command("show running-config")

            http_enabled = "ip http server" in config

            snmp_default = (
                "snmp-server community public" in config or
                "snmp-server community private" in config
            )

            connection.disconnect()

            return http_enabled, snmp_default

        except Exception as e:
            print(f"[ERROR] Connection failed to {device['host']}: {e}")
            return "ERROR", "ERROR"

def generate_report(results):
    filename = f"Audit_Report_{datetime.now().date()}.txt"

    with open(filename, "w") as f:
        f.write("--- Network Device Audit Report ---\n")

        for r in results:
            f.write(f"\nDevice: {r['device']}\n")
            f.write(f"- Telnet Status: {r['telnet']}\n")
            f.write(f"- HTTP Server Status: {r['http']}\n")
            f.write(f"- SNMP Status: {r['snmp']}\n")

    print(f"\n Audit report saved to {filename}")

def main():
    results = []

    for device in devices:
        ip = device["host"]

        print(f"🔍 Checking device: {ip}")


        telnet_port, http_port = scan_ports(ip)


        http_config, snmp_default = check_device_config(device)


        telnet_status = (
            "Telnet is enabled" if telnet_port == "open"
            else "Telnet is disabled"
        )


        if http_config == "ERROR":
            http_status = "Connection failed"
            snmp_status = "Connection failed"
        else:
            http_status = (
                "HTTP server is enabled"
                if http_config else "HTTP server is disabled"
            )

            snmp_status = (
                "Default SNMP community strings found"
                if snmp_default
                else "No default SNMP community strings found"
            )

        results.append({
            "device": ip,
            "telnet": telnet_status,
            "http": http_status,
            "snmp": snmp_status
        })

    generate_report(results)

if __name__ == "__main__":
    main()