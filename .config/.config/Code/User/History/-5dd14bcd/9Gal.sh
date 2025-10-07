#!/usr/bin/env bash

status=$(nmcli radio wifi)
if [[ $status == 'disabled' ]]; then
    nmcli radio wifi on
    notify-send 'Wi-Fi Enabled' -r 1125
fi

# Trigger a rescan in background
nmcli device wifi rescan >/dev/null 2>&1 &

# Capture wifi list (skip header row)
networks=$(nmcli -t -f SSID,SIGNAL device wifi list | awk -F: 'length($1) > 0 {print $2 "% " $1}')

if [[ -z $networks ]]; then
    notify-send 'Wi-Fi' 'No networks found'
    exit 1
fi

# Let user pick with fzf
choice=$(echo "$networks" | sort -nr | fzf --prompt="Wi-Fi: " --header="Signal | SSID" --with-nth=2..)

[[ -z $choice ]] && exit 0

# Extract SSID (field after signal%)
ssid=$(echo "$choice" | cut -d' ' -f2-)

echo "Connecting to $ssid..."
if nmcli device wifi connect "$ssid" --ask; then
    notify-send 'Wi-Fi' "Connected to $ssid"
else
    notify-send 'Wi-Fi' "Failed to connect to $ssid"
fi
