#! /usr/bin/env python3
import json
import jsonschema
import sys
import os
import argparse
import logging

def validate_single_file(json_fp, schema):
    try:
        equajson = json.load(json_fp)
    except:
        logging.error("Invalid JSON in file: {}".format(json_fp.name))
        raise
    try:
        jsonschema.validate(equajson, schema)
    except jsonschema.exceptions.ValidationError:
        logging.error("in file: {}".format(json_fp.name))
        raise
    basename_no_extension = os.path.splitext(os.path.basename(json_fp.name))[0]

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
    parser.add_argument(
        '-v',
        '--verbose',
        help='More verbose logging',
        dest="loglevel",
        default=logging.WARNING,
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        '-d',
        '--debug',
        help='Enable debugging logs',
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
    )
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    equajson_path = args.json_file
    schema_path = args.schema

    with open(schema_path) as schema_file:
            try:
                equajson_schema = json.load(schema_file)
            except:
                logging.error("in file: {}".format(schema_path))
                raise

    with open(equajson_path) as json_file:
        validate_single_file(json_file, equajson_schema)

if __name__ == '__main__':
    main()
