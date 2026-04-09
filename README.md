# Python Training Codeline
This repository contains all exercises, projects, and tasks completed during the Python training course. The course was conducted over two weeks:

Week 1: Focused on basic networking concepts, including IP address validation, subnet calculations, log analysis, and server programming.

Week 2: Explored advanced networking and security operations using libraries like nmap, paramiko, and netmiko for network scanning, SSH key management, device configuration backup, and security auditing.


## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd python-course-linecode
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Course Structure

### Day 1: Introduction to Python Networking

- `activities.py`: Basic networking activities
- `ip_validator.py`: IP address validation utilities

### Day 2: Subnet Calculation
- `subnet-calculator.py`: Tools for subnet calculations and IP range analysis

### Day 3: Log Analysis
- `log-analyzer.py`: Script to analyze log files for security events
- `notes.py`: Additional notes and utilities
- Output files: `output.csv`, `output.json`, `threats.txt`

### Day 4: Advanced Networking Concepts
*(Content to be added)*

### Day 5: Server Programming
- `server.py`: Basic server implementation

### Day 6: Network Time and Reachability
- `get_time_to_reach.py`: Tools to measure network reachability and timing

### Day 7: SSH Key Management
- `ssh_key.py`: SSH key generation and management utilities

### Day 8: Network Scanning
- `ping-scan.py`: Ping sweep and basic network scanning

### Day 9: Final Scanner
- `final_scanner.py`: Comprehensive network scanning tool

### Day 10: Security Auditing
- `audit.py`: System and network auditing scripts


## Usage

Each day's directory contains Python scripts. Run them using:

```bash
python Day1/activities.py
```
