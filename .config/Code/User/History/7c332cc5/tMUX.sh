#!/bin/bash

bars="▁▂▃▄▅▆▇█"
while read -r line; do
    out=""
    for value in $line; do
        index=$((value / 32))
        [[ $index -ge ${#bars} ]] && index=$((${#bars} - 1))
        out+="${bars:$index:1}"
    done
    echo "{\"text\": \"$out\"}"
done < <(cava -p ~/.config/cava/config | grep --line-buffered -v "^#")
