#!/usr/bin/env bash

# Start fzf immediately with "Scanning..." and allow reload
selection=$(
    echo "Scanning Wi-Fi networks..." |
    fzf --prompt="Wi-Fi: " --height=20 --reverse --border \
        --bind "change:reload(nmcli -t -f SSID,SIGNAL,SECURITY device wifi list \
                | awk -F: '{printf \"%-30s  %3s%%  %s\n\", \$1, \$2, \$3}' | uniq || echo 'Scanning...')"
)

# Exit if nothing selected
[[ -z "$selection" ]] && exit 1

# Extract SSID
ssid=$(echo "$selection" | awk '{print $1}')

# Connect
if [[ -n "$ssid" ]]; then
    nmcli device wifi connect "$ssid" --ask
fi
