#!/bin/bash

options=" Lock\n Logout\n Reboot\n Shutdown\n Suspend"
choice=$(echo -e "$options" | wofi --dmenu --prompt "Choose:" --width 300 --height 300 --hide-scroll)

case "$choice" in
    " Lock") hyprlock ;;
    " Logout") hyprctl dispatch exit ;;
    " Reboot") systemctl reboot ;;
    " Shutdown") systemctl poweroff ;;
    " Suspend") systemctl suspend ;;
esac
