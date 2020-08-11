#! /usr/bin/env python3
import json
import jsonschema
import sys
import os
import argparse

def main():
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

    equajson_path = args.json_file
    schema_path = args.schema

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

if __name__ == '__main__':
    main()
