#!/usr/bin/env bash

# Get Wi-Fi interface
iface=$(nmcli device status | awk '/wifi/ {print $1; exit}')

# List networks: SSID | Signal%
networks=$(nmcli -t -f SSID,SIGNAL dev wifi list ifname "$iface" | sort -r -k2)

# Exit if no networks found
[[ -z "$networks" ]] && exit 1

# Use fzf inside kitty for selection
chosen=$(echo "$networks" | awk -F: '{print $1 " (" $2 "%)"}' | kitty sh -c "fzf --prompt='Wi-Fi: ' --height=40% --reverse")

# Extract SSID from selection
ssid=$(echo "$chosen" | sed 's/ (.*)//')

# Connect to selected network
if [[ -n "$ssid" ]]; then
    nmcli device wifi connect "$ssid"
fi
