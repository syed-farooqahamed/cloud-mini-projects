# CPU Usage Logger

This is a simple Python script that logs CPU usage values entered by the user.

## 🧠 Features
- Takes multiple CPU usage values from the user
- Logs whether each value is HIGH (>70%) or NORMAL
- Adds a timestamp to every log entry
- Appends all entries to `cpu_log.txt`

## 🛠️ How It Works
1. The user inputs how many CPU values they want to log.
2. For each value:
   - If CPU usage > 70%, it's marked **HIGH**
   - Otherwise, it's marked **NORMAL**
3. Each entry is saved with a timestamp in `cpu_log.txt`
