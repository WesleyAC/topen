#!/bin/sh
curl `echo $1 | sed "s/gifv/mp4/g"` | mplayer -fs -
