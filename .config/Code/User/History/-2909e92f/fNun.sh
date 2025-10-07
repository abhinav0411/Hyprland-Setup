#!/bin/bash
case "$1" in
  up) pactl set-source-volume @DEFAULT_SOURCE@ +5% ;;
  down) pactl set-source-volume @DEFAULT_SOURCE@ -5% ;;
  toggle) pactl set-source-mute @DEFAULT_SOURCE@ toggle ;;
esac
