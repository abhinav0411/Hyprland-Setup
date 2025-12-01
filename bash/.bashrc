# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]; then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
if [ -d ~/.bashrc.d ]; then
    for rc in ~/.bashrc.d/*; do
        if [ -f "$rc" ]; then
            . "$rc"
        fi
    done
fi
unset rc

export PATH=$PATH:/home/abhinav/.spicetify


fixerror() {
    last_cmd=$(fc -ln -1)

    if [ -z "$last_cmd" ]; then
        /home/abhinav/Desktop/shell-script/fixerror/venv/bin/python \
            /home/abhinav/Desktop/shell-script/fixerror/aihelp.py
    else
        /home/abhinav/Desktop/shell-script/fixerror/venv/bin/python \
            /home/abhinav/Desktop/shell-script/fixerror/aihelp.py "$last_cmd"
    fi
}


# bun
export BUN_INSTALL="$HOME/.local/share/reflex/bun"
export PATH="$BUN_INSTALL/bin:$PATH"
export PATH=$PATH:/usr/local/go/bin
