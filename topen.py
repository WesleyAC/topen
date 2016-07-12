#!/usr/bin/python
import sys
import os
import re
import subprocess

if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] + " url\nI only take one argument, but you proveded " + str(len(sys.argv)-1) + "!")
    sys.exit(1)

url = sys.argv[1]
script_path = os.path.dirname(os.path.realpath(__file__))

helpers = [
    [r"http(s)?://[A-Za-z0-9\-\.]+\.[A-Za-z]+/.*(\.png|\.jpg|\.jpeg)$", "generic-image.sh"],
    [r"http(s)?://(i\.)?imgur\.com/[\w]+\.gifv", "imgur-gifv.sh"],
    [r"http(s)?://(i\.)?imgur\.com/[\w]+(/)?$", "imgur-single.sh"],
    [r"http(s)?://(www\.)?youtube\.com/watch.", "youtube.sh"],
    [r"http(s)?://gfycat\.com/[a-zA-Z]", "gfycat.sh"],
    [r"http(s)?://[A-Za-z0-9\-\.]+\.[A-Za-z]+/.*\.mp4$", "generic-mp4.sh"],
    [r"http(s)?://[A-Za-z0-9\-\.]+\.[A-Za-z]+.", "generic.sh"],
]

for helper in helpers:
    if re.compile(helper[0]).match(url):
        if not bool(os.environ.get("DISPLAY")):
            os.putenv("DISPLAY", subprocess.check_output([script_path + "/getdisplay.sh"])[0:-1])
        subprocess.run([script_path + "/helpers/" + helper[1], url])
        sys.exit(0)

print("Error: No helper script found!\nPlease check that the url is valid.")
sys.exit(1)
