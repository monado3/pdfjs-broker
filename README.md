pdfjs-broker
---
CLI-tool which opens a pdf file specified by command line argument in the form of URI with pdf.js.

# Requirements
- docker environment

# Installation
1. `$ git clone {this repository}`
1. `$ cd pdfjs_server && docker build -t pdfjs .`
1. Add $BROWSER={your browser you want to use for reading pdf} to environment variable

# Usage
`$ ./broker.py {URL of pdf file you want to read}`

*I recommend setting the alias to `broker.py`*
