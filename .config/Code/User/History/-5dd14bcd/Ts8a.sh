#!/usr/bin/env bash
#
# Wi-Fi menu using nmcli + fzf in kitty

# Ensure Wi-Fi is enabled
if [[ $(nmcli radio wifi) == "disabled" ]]; then
    nmcli radio wifi on
    notify-send 'Wi-Fi Enabled' -r 1125
fi

# Rescan for networks
nmcli device wifi rescan >/dev/null 2>&1

# Collect networks
output=$(nmcli device wifi list)
list=$(tail -n +2 <<<"$output" | awk '$2 != "--"')

if [[ -z $list ]]; then
    notify-send 'Wi-Fi' 'No networks found'
    exit 1
fi

# Header row
header=$(head -n 1 <<<"$output")

# Launch inside kitty with fzf
choice=$(kitty sh -c "echo \"$list\" | fzf --ansi \
    --border=sharp \
    --header='$header' \
    --height=100% \
    --reverse \
    --pointer='➤ ' \
    --info=inline-right")

# Get BSSID (first column)
bssid=$(awk '{print $1}' <<<"$choice")

[[ -z $bssid ]] && exit 0

# Connect
if nmcli device wifi connect "$bssid" --ask; then
    notify-send 'Wi-Fi' 'Successfully connected'
else
    notify-send 'Wi-Fi' 'Failed to connect'
fi
