#!/bin/bash
vol=$(pactl get-sink-volume @DEFAULT_SINK@ | grep -oP '\d+%' | head -1 | tr -d '%')
options="Mute\n[■■■■□□□□] 50%\n[■■■■■□□□] 60%\n[■■■■■■■■] 100%"

chosen=$(echo -e "$options" | wofi --dmenu --prompt "Volume:")

case $chosen in
  "Mute") pactl set-sink-mute @DEFAULT_SINK@ toggle ;;
  *% ) pactl set-sink-volume @DEFAULT_SINK@ "$(echo $chosen | grep -o '[0-9]\+%')" ;;
esac
