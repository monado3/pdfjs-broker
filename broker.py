#!/usr/bin/python3
import argparse
import socket
import subprocess as subp

from pathlib import Path


def is_free(port_n: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(('localhost', port_n))
        sock.close()
        return True
    except OSError:
        return False


def search_min_open_port(n_min: int) -> int:
    for i in range(n_min, 60000):
        if is_free(i):
            return i


def exec_pdfjs_ctn_url(pdf_url: str, n_port: int):
    proc = subp.Popen(['docker', 'run', '-itd', '--rm', '-p',
                       f'{n_port}:8080', '--name', f'pdfjs_{n_port}', 'pdfjs_url', pdf_url], stdout=subp.DEVNULL, stderr=subp.DEVNULL)


def exec_pdfjs_ctn_file(pdf_path: str, n_port: int):
    ctn_name = f'pdfjs_{n_port}'
    proc = subp.Popen(
        ['docker', 'run', '-itd', '--rm', '-p',
            f'{n_port}:8080', '-v', f'{pdf_path}:/pdfjs/web/downloaded.pdf', '--name', ctn_name, 'pdfjs_file'],
        stdout=subp.DEVNULL,
        stderr=subp.DEVNULL
    )


def init_argparser():
    parser = argparse.ArgumentParser(
        prog='broker.py',
        usage='pdfjs [-u <URL> | -f <filepath>]',
        description='Open a pdf in a broweser by pdfjs',
        add_help=True,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-u', '--url',
        help='URL of a pdf',
        action='store',
        type=str,
        dest='url',
    )
    group.add_argument(
        '-f', '--file',
        help='local filepath of a pdf',
        action='store',
        type=str,
        dest='path',
    )
    return parser


if __name__ == '__main__':
    parser = init_argparser()
    args = parser.parse_args()
    n_port = search_min_open_port(50000)
    if args.url:
        url = args.url
        exec_pdfjs_ctn_url(url, n_port)
    else:
        filepath = (Path.cwd() / args.path).resolve()
        exec_pdfjs_ctn_file(str(filepath), n_port)
    subp.run(f'$BROWSER http://localhost:{n_port}/web/viewer.html?file=downloaded.pdf',
             shell=True, stdout=subp.DEVNULL, stderr=subp.DEVNULL)
