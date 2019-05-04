FROM php:latest


RUN apt-get update && apt-get install -y \
    wget \
    unzip

ARG pdfjs_zip_uri="https://github.com/mozilla/pdf.js/releases/download/v2.0.943/pdfjs-2.0.943-dist.zip"

RUN wget ${pdfjs_zip_uri} -O /pdfjs.zip
RUN unzip /pdfjs.zip -d /pdfjs
RUN rm -rf /pdfjs.zip

WORKDIR pdfjs

ADD ./main.sh /

ENTRYPOINT [ "/main.sh" ]
CMD []
