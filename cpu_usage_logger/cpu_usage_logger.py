def cpu_usage(n):
    file=open("cpu_log.txt", "a"):
        if n >= 70:
            file.write(f"CPU {n}%: High usage\n")
        else:
            file.write(f"CPU {n}%: Normal\n")

n = int(input("Enter CPU usage %: "))
cpu_usage(n)
