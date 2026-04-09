def mock_scan_ports(ip):
    """
    Simulates Nmap scan results
    """
    if ip.endswith("10"):
        return "open", "closed"   
    else:
        return "closed", "open"   


def mock_check_device_config(device):
    """
    Simulates Netmiko config results
    """
    if device["host"].endswith("10"):
        return False, False   
    else:
        return True, True    