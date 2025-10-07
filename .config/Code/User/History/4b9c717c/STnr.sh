chosen = $(printf "Performance\n Balanced\n Power Saver" | rofi -dmenu -i -p "Power Menu:")


case chosen in
    "⚡ Performance") powerprofilesctl set performance ;;
    " Balanced")   powerprofilesctl set balanced ;;
    " Power Saver") powerprofilesctl set power-saver ;;
esac