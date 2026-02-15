import argparse
from .converter import number_to_words


def main():
    parser = argparse.ArgumentParser(description="Convert number to words")
    parser.add_argument("number")
    parser.add_argument("--lang", default="fa")
    parser.add_argument("--currency", default=None)
    parser.add_argument("--mode", default="normal")

    args = parser.parse_args()

    result = number_to_words(
        args.number,
        lang=args.lang,
        currency=args.currency,
        mode=args.mode,
    )

    print(result)
