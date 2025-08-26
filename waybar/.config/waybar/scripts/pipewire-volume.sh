#!/bin/bash

# Default sink (speakers/headphones)
VOLUME=$(wpctl get-volume @DEFAULT_AUDIO_SINK@)

# Extract number and mute status
LEVEL=$(echo $VOLUME | awk '{print $2*100}')
MUTED=$(echo $VOLUME | grep -o '\[MUTED\]')

if [ "$MUTED" = "[MUTED]" ]; then
    ICON="󰖁"  # Muted icon
else
    if [ "$LEVEL" -gt 70 ]; then
        ICON="󰕾"  # High volume
    elif [ "$LEVEL" -gt 30 ]; then
        ICON="󰖀"  # Medium volume
    else
        ICON="󰕿"  # Low volume
    fi
fi

echo "{\"text\": \"${ICON} ${LEVEL}%\", \"tooltip\": \"Volume: ${LEVEL}%\"}"
