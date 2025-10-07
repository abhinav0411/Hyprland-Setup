#!/bin/bash

CHOICE=$(wofi --dmenu --prompt "Search or launch:" < <(compgen -c | sort -u))

if command -v "$CHOICE" &> /dev/null; then
    exec "$CHOICE"
else
    xdg-open "https://google.com/search?q=${CHOICE// /+}"
fi
