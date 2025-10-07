#!/usr/bin/env bash

# Relaunch inside kitty if not already there
if [[ -z "$KITTY_WINDOW_ID" ]]; then
    exec kitty --hold bash -c "$0"
fi

chosen=$(printf "⚡ Performance\n Balanced\n Power Saver" | fzf --prompt="Power Menu: ")

case "$chosen" in
    "⚡ Performance") powerprofilesctl set performance ;;
    " Balanced")    powerprofilesctl set balanced ;;
    " Power Saver") powerprofilesctl set power-saver ;;
esac
