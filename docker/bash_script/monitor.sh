#!/bin/bash
# Monitorizare CPU, RAM și Disk

while true; do
    echo "-------------------------------------"
    echo "Data și ora: $(date)"
    echo "CPU Usage: $(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')%"
    echo "Memorie RAM: $(free -m | awk 'NR==2{printf "%.2f%%", $3*100/$2 }')"
    echo "Disk Usage: $(df -h / | awk 'NR==2{print $5}')"
    echo "-------------------------------------"
    sleep 5
done
