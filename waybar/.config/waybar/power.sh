#!/usr/bin/env bash
#
# Power profile switcher using fzf

# Get current mode
current=$(powerprofilesctl get)

# Build menu
profiles=(
    "performance "
    "balanced "
    "power-saver "
)

# Mark current profile
menu=""
for p in "${profiles[@]}"; do
    if [[ $p == $current* ]]; then
        menu+="$p (current)\n"
    else
        menu+="$p\n"
    fi
done

# Options for fzf
options=(
    --border=sharp
    --border-label=' Power Profiles '
    --height=20
    --reverse
    --pointer="👉"
    --header="Current profile: $current"
)

choice=$(echo -e "$menu" | fzf "${options[@]}" | awk '{print $1}')

[[ -z $choice ]] && exit 0

# Apply selected profile
if powerprofilesctl set "$choice"; then
    notify-send "Power Profile" "Switched to $choice"
else
    notify-send "Power Profile" "Failed to set $choice"
fi
