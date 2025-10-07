#!/bin/bash

options="Lock\nShutdown\nReboot\nLogout\nCancel"
selected=$(echo -e $options | wofi --dmenu --prompt "Power Menu" --width 200 --height 200 --hide-scroll --insensitive)

case $selected in
  Lock) hyprlock ;;
  Shutdown) systemctl poweroff ;;
  Reboot) systemctl reboot ;;
  Logout) hyprctl dispatch exit ;;
  Cancel) exit 0 ;;
  *) exit 1 ;;
esac
