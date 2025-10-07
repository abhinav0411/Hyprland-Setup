#!/bin/bash

bars=(▁ ▂ ▃ ▄ ▅ ▆ ▇ █)
while true; do
    output=""
    for i in {1..16}; do
        rand=$((RANDOM % 8))
        output+="${bars[$rand]}"
    done
    echo "{\"text\": \"$output\"}"
    sleep 0.2
done
