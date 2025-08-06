import psutil
import logging

logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format='%(asctime)s-%(levelname)s-%(message)s'
)

cpu=int(psutil.cpu_percent(interval=1))
if cpu<70:
    logging.info(f"CPU usage is normal: {cpu}%")
elif cpu<90:
    logging.warning(f"CPU usage is high: {cpu}%")
else:
    logging.error(f"CPU usage is critical: {cpu}%")

ram=int(psutil.virtual_memory().percent)
if ram<70:
    logging.info(f"RAM usage is normal: {ram}%")
elif ram<90:
    logging.warning(f"RAM usage is high: {ram}%")
else:
    logging.error(f"RAM usage is critical: {ram}%")

disk=int(psutil.disk_usage('/').percent)
if disk<70:
    logging.info(f"Disk usage is normal: {disk}%")
elif disk<90:
    logging.warning(f"Disk usage is high: {disk}%")
else:
    logging.error(f"Disk usage is critical: {disk}%")