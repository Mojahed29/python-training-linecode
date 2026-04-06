import csv
import json


log_data = """2024-11-01 08:01:12 ACCEPT TCP SRC=192.168.1.10 SPT=54321 DST=10.0.0.5 DPT=80 LEN=52
2024-11-01 08:01:45 DROP TCP SRC=203.0.113.42 SPT=6000 DST=10.0.0.5 DPT=22 LEN=40
2024-11-01 08:02:10 ACCEPT UDP SRC=192.168.1.15 SPT=1025 DST=8.8.8.8 DPT=53 LEN=72
2024-11-01 08:03:05 DROP TCP SRC=203.0.113.42 SPT=6001 DST=10.0.0.5 DPT=443 LEN=40
2024-11-01 08:04:22 ACCEPT TCP SRC=192.168.1.10 SPT=54400 DST=10.0.0.5 DPT=443 LEN=60
2024-11-01 08:05:01 DROP TCP SRC=198.51.100.9 SPT=9999 DST=10.0.0.5 DPT=3306 LEN=40
2024-11-01 08:05:45 CORRUPTED ENTRY - IGNORE THIS
2024-11-01 08:06:30 DROP TCP SRC=203.0.113.42 SPT=6100 DST=10.0.0.5 DPT=80 LEN=40
2024-11-01 08:07:10 ACCEPT TCP SRC=192.168.1.20 SPT=2048 DST=172.16.0.1 DPT=8080 LEN=80
2024-11-01 08:08:55 DROP UDP SRC=198.51.100.9 SPT=1234 DST=10.0.0.5 DPT=53 LEN=28
"""

with open("firewall.log", "w") as f:
    f.write(log_data)

entries = []
malformed = 0

with open("firewall.log", "r") as f:
    for line in f:
        p = line.strip().split()  

        if len(p) == 9 and p[2] in ["ACCEPT", "DROP"]:
            entries.append({
                "timestamp":        p[0] + " " + p[1],
                "action":           p[2],
                "protocol":         p[3],
                "source_ip":        p[4].split("=")[1],
                "source_port":      p[5].split("=")[1],
                "destination_ip":   p[6].split("=")[1],
                "destination_port": p[7].split("=")[1],
                "packet_size":      p[8].split("=")[1],
            })
        elif line.strip() != "":
            malformed += 1


accept_count = 0
drop_count   = 0
port_hits    = {}
ip_count     = {}

for e in entries:

    if e["action"] == "ACCEPT":
        accept_count += 1
    else:
        drop_count += 1

    port = e["destination_port"]
    port_hits[port] = port_hits.get(port, 0) + 1

    ip = e["source_ip"]
    ip_count[ip] = ip_count.get(ip, 0) + 1

top_3        = sorted(port_hits.items(), key=lambda x: x[1], reverse=True)[:3]
suspicious   = {ip: c for ip, c in ip_count.items() if c >= 3}


with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Timestamp","Action","Protocol","Source IP","Source Port","Destination IP","Destination Port","Packet Size"])
    for e in entries:
        writer.writerow([e["timestamp"], e["action"], e["protocol"], e["source_ip"], e["source_port"], e["destination_ip"], e["destination_port"], e["packet_size"]])


with open("output.json", "w") as f:
    json.dump(entries, f, indent=4)


with open("threats.txt", "w") as f:
    f.write("THREAT REPORT\n")
    f.write("=" * 48 + "\n")
    f.write("Suspicious IPs (3+ log appearances):\n\n")
    for ip, count in suspicious.items():
        f.write("IP: " + ip + " | Occurrences: " + str(count) + "\n")


print("=" * 60)
print("FIREWALL LOG ANALYSIS REPORT")
print("=" * 60)
print("Total entries processed  :", len(entries) + malformed)
print("Valid entries parsed     :", len(entries))
print("Malformed entries skipped:", malformed)
print("\n--- Action Summary ---")
print("ACCEPT :", accept_count)
print("DROP   :", drop_count)
print("\n--- Top 3 Targeted Destination Ports ---")
for i, (port, hits) in enumerate(top_3, 1):
    print(str(i) + ". Port " + port + " - " + str(hits) + " hits")
print("\n--- Suspicious Source IPs (3+ appearances) ---")
for ip, count in suspicious.items():
    print(ip + " - " + str(count) + " occurrences")
print("\nOutput saved: output.csv | output.json | threats.txt")
print("=" * 60)