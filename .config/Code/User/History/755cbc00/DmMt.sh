#!/bin/bash
options="Mute\nVolume Up\nVolume Down"
chosen=$(echo -e "$options" | wofi --dmenu --prompt "Audio:")

case $chosen in
  "Mute") pactl set-sink-mute @DEFAULT_SINK@ toggle ;;
  "Volume Up") pactl set-sink-volume @DEFAULT_SINK@ +5% ;;
  "Volume Down") pactl set-sink-volume @DEFAULT_SINK@ -5% ;;
esac
