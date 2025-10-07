#!/usr/bin/env bash

export DBUS_SESSION_BUS_ADDRESS='unix:path=/run/user/1000/bus'

case $1 in
	'charging')
		state='Charging'
		icon='battery-full-charging'
		;;
	'discharging')
		state='Discharging'
		icon='battery-full'
		;;
esac

path=$(upower -e | grep BAT | head -n 1)
level=$(upower -i "$path" | awk '/percentage:/ {print $2}')

notify-send "Battery ${state} (${level})" -i "$icon" -r 1525