# Python Logging Monitor

This mini project is a basic system monitoring script written in Python. It logs CPU, RAM, and Disk usage to a log file using Python's built-in `logging` module.

## 🚀 What It Does

- Checks real-time system usage:
  - ✅ CPU Usage
  - ✅ RAM Usage
  - ✅ Disk Usage
- Logs the data into a file called `system.log`
- Uses log levels to report status:
  - `INFO` – normal usage
  - `WARNING` – high usage
  - `ERROR` – critical usage
- Adds timestamps to each log entry

## 🧰 Tools Used

- Python 3
- `psutil` module (for system data)
- `logging` module (for file logging)
