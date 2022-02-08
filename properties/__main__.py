import argparse
import json

from . import load


def main() -> None:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("file", help="Path to the properties file")

    args = arg_parser.parse_args()

    print(json.dumps(load(args.file), indent=2))


if __name__ == "__main__":  # pragma: no cover
    main()
