#!/usr/bin/env bash

# Get Wi-Fi interface
iface=$(nmcli device status | awk '/wifi/ {print $1; exit}')

# List networks: SSID | Signal%
networks=$(nmcli -t -f SSID,SIGNAL dev wifi list ifname "$iface" | sort -r -k2)

# Exit if no networks found
[[ -z "$networks" ]] && exit 1

# Choose network with rofi
chosen=$(echo "$networks" | awk -F: '{print $1 " (" $2 "%)"}' | rofi -dmenu -i -p "Wi-Fi:")

# Extract SSID from selection
ssid=$(echo "$chosen" | sed 's/ (.*)//')

# Connect to selected network
if [[ -n "$ssid" ]]; then
    # Ask for password if needed
    nmcli device wifi connect "$ssid"
fi
