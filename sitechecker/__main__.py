import sys
import pathlib
from asyncore import read

from sitechecker.checker import site_is_online
from sitechecker.cli import read_user_cli_args, display_check_result


def main():
    """Verificando disponibilidade de site"""
    user_args = read_user_cli_args()
    urls = user_args.urls
    if not urls:
        print("Erro! Insira url para análise.", file=sys.stderr)
        sys.exit(1)
    _site_check(urls)


def _site_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)

if __name__ == "__main__":
    main()

