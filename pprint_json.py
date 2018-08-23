import json
import argparse
import os
import sys


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='Path of JSON file')
    return parser


def load_data(filepath):
    with open(filepath, 'r') as file:
        try:
            decoded_json = json.load(file)
            return decoded_json
        except json.decoder.JSONDecodeError:
            return None


def pretty_print_json(decoded_json):
    formated_json = json.dumps(
        decoded_json,
        indent=2,
        ensure_ascii=False
    )
    print(formated_json)


if __name__ == '__main__':

    parser = create_arg_parser()
    args = parser.parse_args()
    filepath = os.path.abspath(args.file)

    decoded_json = load_data(filepath)
    if decoded_json is None:
        sys.exit('Load error. JSON file is incorrect.')

    pretty_print_json(decoded_json)
