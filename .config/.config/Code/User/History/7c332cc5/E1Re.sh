#!/bin/bash

bars=(▁ ▂ ▃ ▄ ▅ ▆ ▇ █)

cava -p ~/.config/cava/config | while read -r line; do
    output=""
    for val in $line; do
        if [[ "$val" =~ ^[0-9]+$ ]]; then
            index=$(( val * ${#bars[@]} / 255 ))
            (( index >= ${#bars[@]} )) && index=$((${#bars[@]} - 1))
            output+="${bars[$index]}"
        fi
    done
    echo "RAW LINE: $line" >&2
done
