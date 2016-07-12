#!/bin/sh
youtube-dl -o - $1 | mplayer -fs -
