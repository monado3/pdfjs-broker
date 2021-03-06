# pdfjs-broker
---
CLI-tool which opens a pdf file specified by command line argument in the form of URL or local filepath with pdf.js.

# Requirements
- docker environment (You have to be able to execute docker commands without `sudo`)
- Python 3 (>=3.6)
- browser-launcing command depending on your platform
    - `wslview` on WSL
    - Environment variable `$BROWSER` (e.g. `$BROWSER=chromium` ) on Linux 

# Installation
1. `$ git clone git@github.com:monado3/pdfjs-broker.git`
1. `$ cd pdfjs-broker`
1. `$ docker build -t pdfjs_url ./pdfjs_server_url`
1. `$ docker build -t pdfjs_file ./pdfjs_server_file`
1. Configure browser launcing
    - Add $BROWSER={your browser you want to use for reading pdf files} to environment variable (on Linux)
    - install `wslu` for `wslview` command (on WSL)
1. `$ ln -s {/foo/bar/broker.py} /usr/local/bin/pdfjs`

# Usage
`$ pdfjs [-u <URL of a pdf file> | -f <pdf file path>]`
