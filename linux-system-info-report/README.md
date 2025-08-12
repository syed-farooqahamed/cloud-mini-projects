# Linux System Info Report 🖥️

A Bash-based system monitoring script that collects important system information and saves it into a timestamped report file.  
Includes an optional email feature for automated reporting.

## 📌 Features
- **Disk Usage** (`df -h`)
- **Memory Usage** (`free -h`)
- **Top 5 CPU-using Processes** (`ps`)
- **Recent System Errors** (`grep` from syslog)
- Saves report with **timestamped filename**
- Optional **email sending** (requires `mailutils`)

## 🚀 Usage
1. Make script executable:
```bash
chmod +x system_info_report.sh
