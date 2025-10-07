#!/bin/bash
current=$(pactl get-sink-volume @DEFAULT_SINK@ | grep -oP '\d+%' | head -1 | tr -d '%')

new=$(yad --scale --value="$current" --min-value=0 --max-value=100 --step=1 \
          --title="Volume" --window-icon=audio-volume-high \
          --undecorated --no-buttons --geometry=200x50+960+30) # tweak geometry

if [ -n "$new" ]; then
  pactl set-sink-volume @DEFAULT_SINK@ "$new"%
fi
