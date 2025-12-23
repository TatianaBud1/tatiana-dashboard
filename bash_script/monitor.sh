#!/bin/bash

# Folder date (relativ la script)
DATA_DIR="../python_script/data"

# Asigură-te că există folderul
mkdir -p "$DATA_DIR"
# Fișiere
HISTORY_FILE="$DATA_DIR/latency_history.tmp"
OUTPUT_FILE="$DATA_DIR/internet_status.json"

while true
do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    TARGET="google.com"
    PING=$(ping -c 1 $TARGET 2>/dev/null)

    if [ $? -ne 0 ]; then
        TARGET="1.1.1.1"
        PING=$(ping -c 1 $TARGET 2>/dev/null)
    fi

    if [ $? -eq 0 ]; then
        STATUS="UP"
        LATENCY=$(echo "$PING" | grep time= | sed 's/.*time=\([0-9.]*\).*/\1/')
    else
        STATUS="DOWN"
        LATENCY=0
    fi

    # Istoric latență
    echo "$LATENCY" >> "$HISTORY_FILE"
    tail -n 10 "$HISTORY_FILE" > "${HISTORY_FILE}.tmp" && mv "${HISTORY_FILE}.tmp" "$HISTORY_FILE"
    HISTORY=$(awk '{printf "%s,", $0}' "$HISTORY_FILE" | sed 's/,$//')

    # Nivel calitate
    if [ "$STATUS" = "DOWN" ]; then
        QUALITY="DOWN"
    elif (( $(echo "$LATENCY < 80" | bc -l) )); then
        QUALITY="OK"
    elif (( $(echo "$LATENCY < 150" | bc -l) )); then
        QUALITY="WARNING"
    else
        QUALITY="BAD"
    fi

    # IP public
    PUBLIC_IP=$(wget -qO- https://api.ipify.org || echo "unknown")

    # JSON
    cat <<EOF > "$OUTPUT_FILE"
{
  "internet": {
    "status": "$STATUS",
    "quality": "$QUALITY",
    "latency_ms": $LATENCY,
    "target": "$TARGET"
  },
  "latency_history": [$HISTORY],
  "public_ip": "$PUBLIC_IP",
  "last_check": "$TIMESTAMP"
}
EOF

    echo "[$TIMESTAMP] Internet: $STATUS | $LATENCY ms | $QUALITY"

    sleep 5
done
