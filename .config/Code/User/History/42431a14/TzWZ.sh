#!/bin/bash
case "$1" in
  up) pactl set-sink-volume @DEFAULT_SINK@ +5% ;;
  down) pactl set-sink-volume @DEFAULT_SINK@ -5% ;;
  toggle) pactl set-sink-mute @DEFAULT_SINK@ toggle ;;
esac
