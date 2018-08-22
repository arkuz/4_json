import json
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("file", help="Path of JSON file")
args = parser.parse_args()
filepath = os.path.abspath(args.file)


def load_data(filepath):
    with open(filepath, 'r') as file:
        try:
            json_file = json.load(file)
            return json_file
        except json.decoder.JSONDecodeError:
            return None


def pretty_print_json(data):
    formated_json = json.dumps(data,
                               indent=2,
                               ensure_ascii=False)
    print(formated_json)


if __name__ == '__main__':
    data = load_data(filepath)
    if data is None:
        print("Load error. JSON file is incorrect.")
        exit()

    pretty_print_json(data)
