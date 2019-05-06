#!/bin/bash
docker run -it --rm -p 8080:8080 pdfjs $1
$BROWSER http://localhost:8080/web/viewer.html?file=downloaded.pdf
