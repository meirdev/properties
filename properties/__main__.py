import argparse
import json

from . import load


def main() -> None:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("file", help="Path to the properties file")

    args = arg_parser.parse_args()

    with open(args.file) as fp:
        print(json.dumps(load(fp), indent=2))


if __name__ == "__main__":  # pragma: no cover
    main()
