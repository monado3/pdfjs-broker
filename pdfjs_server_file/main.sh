#!/bin/bash

cd /pdfjs

php -S 0.0.0.0:8080 > /dev/null 2>&1
# If you use localhost instead of 0.0.0.0, it doesn't work. You can access from docker container itself, but cannot from local machine.
