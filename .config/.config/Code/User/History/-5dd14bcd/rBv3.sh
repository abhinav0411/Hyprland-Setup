#!/usr/bin/env bash

# Fetch Wi-Fi list
list=$(nmcli -t -f SSID,SIGNAL,SECURITY device wifi list | sed '/^$/d')

# Show SSIDs in fzf (ignore duplicates by uniq - if you want)
selection=$(echo "$list" | awk -F: '{printf "%-30s  %3s%%  %s\n", $1, $2, $3}' | uniq | fzf --prompt="Wi-Fi: " --height=20 --reverse --border)

# Exit if nothing selected
[[ -z "$selection" ]] && exit 1

# Extract SSID (first column)
ssid=$(echo "$selection" | awk '{print $1}')

# Connect to network
if [[ -n "$ssid" ]]; then
    nmcli device wifi connect "$ssid" --ask
fi
