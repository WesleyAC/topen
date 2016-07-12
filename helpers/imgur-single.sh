#!/bin/sh
curl `echo $1 | sed 's/imgur\.com/i\.imgur\.com/g' | sed 's/\/$//g'`.jpg | feh -F -
