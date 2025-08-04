from datetime import datetime
import time
import psutil

def log_system_health():
    try:
        with open ("system_health_log.txt",'a') as file:
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cpu=psutil.cpu_percent(interval=5)
            ram=psutil.virtual_memory().percent
            disk=psutil.disk_usage('/').percent
            file.write(f"CPU usage: {cpu}% at {timestamp} \n")
            file.write(f"RAM usage: {ram}% at {timestamp} \n")
            file.write(f"Disk usage: {disk}% at {timestamp} \n")
            file.write("-------- \n")
    except Exception as e:
        print("Something went wrong!!! " ,e)

try:
    i=int(input("How long do you wanna monitor? (in seconds): "))
    if i<5:
        print("Minimum value is 5 seconds.")
    else:
        for j in range(i//5):
            log_system_health()
        print("Monitoring complete. Logs saved to system_health_log.txt")

except ValueError as e:
    print("Invalid input:", e)


