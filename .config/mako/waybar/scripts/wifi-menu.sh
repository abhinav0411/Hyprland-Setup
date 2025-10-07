#!/bin/bash
# List available Wi-Fi networks
chosen=$(nmcli -t -f SSID dev wifi | grep -v '^--' | sort -u | \
    wofi --dmenu --prompt "Wi-Fi:" --lines=10)

# If something was picked, connect
[ -n "$chosen" ] && nmcli dev wifi connect "$chosen"
