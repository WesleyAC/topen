# topen

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/WesleyAC/topen/blob/master/LICENSE)

`topen` is a small script to open links on the command line. It's designed to be able to view multimedia content (images, videos, gifs, etc) without the overhead of a web browser. `topen` is designed to be used with [rtv](https://github.com/michael-lazar/rtv), but could be useful in other contexts as well.

# How it works

`topen` itself is a very small python script that has a list of regular expressions describing urls, along with a script to deal with the url. Because of this, it's very easy to extend: just add another script to the helpers directory, along with a regexp of sites that it should apply to.

# Supported sites

The default browser is `w3m`. However, there is explicit support for the following sites and cases:

| Site           | Notes                                             |
| -------------- | ------------------------------------------------- |
| Any image link |                                                   |
| Any mp4 file   |                                                   |
| Imgur          | Works with gifv and single images, but not albums |
| Gfycat         | Any gfycat link                                   |

# Dependencies

| Dependency   | Reason                  |
| ------------ | ----------------------- |
| `python`     | Main script             |
| `w3m`        | Default browser         |
| `curl`       | Download images/videos  |
| `feh`        | Display images          |
| `mplayer`    | Display videos          |
| `youtube-dl` | Download youtube videos |

# Contributing

If you find a site that might benefit from having a script for it, submit an issue with the name of the site (and ideally some example links). Or, even better, submit a PR!
