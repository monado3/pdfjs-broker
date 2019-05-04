#!/bin/bash
# echo "$@"
cd /pdfjs
wget "$@" -O web/downloaded.pdf
php -S 0.0.0.0:8080 # If you use localhost instead of 0.0.0.0, it doesn't work. You can access from docker container itself, but cannot from local machine.
