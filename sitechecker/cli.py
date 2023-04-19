import argparse


def read_user_cli_args():
    parser = argparse.ArgumentParser(
        prog="sitechecker", description="Teste se o site está disponível."
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="Insira uma ou mais URLs",
    )
    return parser.parse_args()


def display_check_result(result, url, error=""):
    print(f'Os status do site "{url}" é: ', end =" ")
    if result:
        print('"Online!!"')
    else:
        print(f'"Offline!!"  \n  Erro: "{error}"')