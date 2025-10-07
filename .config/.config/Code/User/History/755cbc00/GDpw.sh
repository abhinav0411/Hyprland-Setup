#!/bin/bash

# Get current volume %
current=$(pactl get-sink-volume @DEFAULT_SINK@ | grep -oP '\d+%' | head -1 | tr -d '%')

# Show a small floating slider (200px wide, 50px tall, top-right position)
new=$(yad --scale \
          --value="$current" \
          --min-value=0 --max-value=100 --step=1 \
          --title="Volume" \
          --undecorated \
          --skip-taskbar \
          --no-buttons \
          --geometry=200x50+1600+30)   # adjust coordinates to your screen/waybar position

# If slider moved → set volume
if [ -n "$new" ]; then
  pactl set-sink-volume @DEFAULT_SINK@ "$new"%
fi
