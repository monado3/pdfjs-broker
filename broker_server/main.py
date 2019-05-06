import subprocess as subp
from flask import *

n_port = 50000

app = Flask(__name__)


@app.route("/<pdf_uri>")
def exec_pdfjs(pdf_uri):

    subp.run(['docker', 'run', '-it', '--rm', '-p', f'{n_port}:8080', 'pdfjs', pdf_uri])


    res = response_204()
    return res

def response_204():
    res = make_response('', 204)
    return res

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=10000, threaded=True)
