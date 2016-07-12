#!/usr/bin/python

import sys
from bs4 import BeautifulSoup
import urllib.request
import subprocess

with urllib.request.urlopen(sys.argv[1]) as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

for tag in soup.find_all(class_="zoom"):
    url = "https:" + tag.img["src"]
    subprocess.run("curl " + url + " | feh -F -", shell=True)
