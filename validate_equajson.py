#! /usr/bin/env python3
import json
import jsonschema
import sys
import os
import argparse

def main(equajson_path, schema_path):

    global filepath

    filepath = equajson_path

    with open(schema_path) as schema_file:
            try:
                equajson_schema = json.load(schema_file)
            except:
                sys.stderr.write("Invalid JSON in schema: `"+schema_file.name+"'"+'\n')
                raise

    with open(equajson_path) as json_file:
            try:
                equajson = json.load(json_file)
            except:
                sys.stderr.write("Invalid JSON in file: `"+json_file.name+"'"+'\n')
                raise
            try:
                jsonschema.validate(equajson, equajson_schema)
            except jsonschema.exceptions.ValidationError:
                sys.stderr.write(json_file.name+'\n')
                raise
            basename_no_extension = os.path.splitext(os.path.basename(json_file.name))[0]

# It's easier to make this a global variable
# than to thread it through every function.
filepath = None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='validate equajson files')
    parser.add_argument(
        '-s',
        '--schema',
        help='path to schema file',
        required=True
    )
    parser.add_argument(
        'json_file',
        help='path to json file to validate'
    )
    args = parser.parse_args()
    main(args.json_file, args.schema)
