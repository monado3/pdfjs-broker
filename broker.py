#!/usr/bin/python3
import socket
import subprocess as subp
import sys

def is_free(port_n: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(('localhost', port_n))
        sock.close()
        return True
    except OSError:
        return False

def search_min_open_port(n_min: int):
    for i in range(n_min, 60000):
        if is_free(i):
            return i

def exec_pdfjs_ctn(pdf_uri:str, n_port:int):
    proc = subp.Popen(['docker', 'run', '-it', '--rm', '-p', f'{n_port}:8080', 'pdfjs', pdf_uri])
    ret = proc.stdout.readline().decode().rstrip()
    return True if ret == 'success' else False

if __name__ == '__main__':
    uri = sys.argv[1]
    n_port = search_min_open_port(50000)
    if exec_pdfjs_ctn(uri, n_port):
        subp.run(f'$BROWSER http://localhost:{n_port}/web/viewer.html?file=downloaded.pdf', shell=True, stdout=subp.DEVNULL, stderr=subp.DEVNULL)
