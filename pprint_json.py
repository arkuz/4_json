import json
import argparse
import os
import sys


def create_arg_parser():
    return argparse.ArgumentParser()


def load_data(filepath):
    with open(filepath, 'r') as file:
        try:
            file_object = json.load(file)
            return file_object
        except json.decoder.JSONDecodeError:
            return None


def pretty_print_json(data_object):
    formated_json = json.dumps(data_object,
                               indent=2,
                               ensure_ascii=False)
    print(formated_json)


if __name__ == '__main__':

    parser = create_arg_parser()
    parser.add_argument("file", help="Path of JSON file")
    args = parser.parse_args()
    filepath = os.path.abspath(args.file)

    data_object = load_data(filepath)
    if data_object is None:
        sys.exit("Load error. JSON file is incorrect.")

    pretty_print_json(data_object)
