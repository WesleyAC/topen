#!/bin/sh
# This script is a workaround to allow rtv to see topen as a terminal a
# terminal program by setting $DISPLAY to an empty value, while setting
# it back for the scripts that it runs.
ps -u $(id -u) -o pid= | \
    while read pid; do
        cat /proc/$pid/environ 2>/dev/null | tr '\0' '\n' | grep '^DISPLAY=:'
    done | grep -o ':[0-9]*' | sort -u | head -n 1
