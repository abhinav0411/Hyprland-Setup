#!/usr/bin/env bash
#
# Wi-Fi menu with instant open (fzf refreshes when scan is done)

# Make sure Wi-Fi is enabled
if [[ $(nmcli radio wifi) == "disabled" ]]; then
    nmcli radio wifi on
    notify-send 'Wi-Fi Enabled' -r 1125
fi

# Launch fzf first (empty list) and feed networks when they arrive
choice=$(kitty sh -c '
    # Run scan in background
    (nmcli device wifi rescan >/dev/null 2>&1 && nmcli -t -f BSSID,SSID,SIGNAL device wifi list) &
    
    # fzf UI opens immediately
    fzf --ansi --border=sharp --header="Scanning Wi-Fi..." \
        --height=100% --reverse --pointer="➤ " --info=inline-right
')

# Extract BSSID (first field)
bssid=$(cut -d: -f1 <<<"$choice")

[[ -z $bssid ]] && exit 0

# Connect
if nmcli device wifi connect "$bssid" --ask; then
    notify-send 'Wi-Fi' 'Successfully connected'
else
    notify-send 'Wi-Fi' 'Failed to connect'
fi
