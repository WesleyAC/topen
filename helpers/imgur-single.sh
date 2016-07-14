#!/bin/sh
curl `echo $1 | sed 's/m\.imgur\.com/i\.imgur\.com/g' | sed 's/[\/]imgur.com/\/i\.imgur\.com/' | sed 's/\/$//g'`.jpg | feh -F -
