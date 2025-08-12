#!/bin/bash
REPORT="system_report_$(date +%Y-%m-%d_%H-%M-%S).txt"
exec > $REPORT

echo "==== System Info Report ===="
date
df -h
echo ""
echo "==== Memory Usage ===="
free -h
echo ""
echo "==== Top 5 Processes by CPU Usage ===="
ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 6
echo ""
echo "==== Recent 'error' Messages from System Logs ===="
grep -i "error" /var/log/syslog | tail -n 5
echo ""
echo "==== Sending report to your email... ===="
mail -s "System Info Report" your_email@example.com < $REPORT
