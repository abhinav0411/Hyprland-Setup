#!/bin/bash

volume=$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk '{print int($2 * 100)}')
mute=$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | grep -c MUTED)

if [ "$mute" -eq 1 ]; then
  echo ""
else
  echo "$volume |"
fi

