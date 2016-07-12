#!/bin/sh
curl `echo $1 | sed "s/gfycat\.com/giant\.gfycat\.com/g"`.mp4 | mplayer -fs -
