from datetime import datetime

def check(cpu_values):
    try:
        with open("cpu_log.txt", "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")      
            if cpu_values > 70:
                file.write(f"[{timestamp}] CPU usage {cpu_values}% is HIGH\n")
            else:
                file.write(f"[{timestamp}] CPU usage {cpu_values}% is NORMAL\n")
    except Exception as e:
        print("Logging error:", e)

try:
    n = int(input("Enter the number of values to input: "))
    for i in range(n):
        try:
            cpu_value = int(input(f"Enter CPU usage value #{i+1}: "))
            check(cpu_value)
        except ValueError:
            print("Invalid CPU value. Please enter a number.")
    print("Logging complete.")
except ValueError:
    print("Please enter a valid number of inputs.")
