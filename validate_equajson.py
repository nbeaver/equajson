#! /usr/bin/env python3
import json
import jsonschema
import sys
import os
import argparse
import logging
import glob

class NoDuplicates:
    """A set that throws an error if a duplicate item is added."""

    def __init__(self, iterable=[]):
        self.set = set()
        for elem in iterable:
            if elem in self.set:
                raise RuntimeError("Duplicate element: " + repr(elem))
            else:
                self.set.add(elem)

    def add(self, elem):
        if elem in self.set:
            raise RuntimeError("Duplicate element: " + repr(elem))
        else:
            self.set.add(elem)


def get_validated_json(json_fp, schema):
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
    return equajson

def readable_directory(path):
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError(
            'not an existing directory: {}'.format(path))
    if not os.access(path, os.R_OK):
        raise argparse.ArgumentTypeError(
            'not a readable directory: {}'.format(path))
    return path

def readable_file(path):
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(
            'not an existing file: {}'.format(path))
    if not os.access(path, os.R_OK):
        raise argparse.ArgumentTypeError(
            'not a readable file: {}'.format(path))
    return path

def main():
    parser = argparse.ArgumentParser(description='validate equajson files')
    parser.add_argument(
        '-s',
        '--schema',
        type=readable_file,
        help='path to schema file',
        required=True
    )
    parser.add_argument(
        'topdir',
        type=readable_directory,
        help='directory of json files to validate'
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

    schema_path = args.schema
    with open(schema_path) as schema_file:
            try:
                equajson_schema = json.load(schema_file)
            except:
                logging.error("in file: {}".format(schema_path))
                raise

    equajson_filepaths = glob.glob(args.topdir + "/*.json")
    uuids = NoDuplicates()
    descriptions = NoDuplicates()
    for i, equajson_filepath in enumerate(equajson_filepaths):
        logging.info("validating file {}".format(equajson_filepath))
        with open(equajson_filepath) as json_fp:
            equajson = get_validated_json(json_fp, equajson_schema)
            uuids.add(equajson["uuid"])
            descriptions.add(equajson["description"]["verbose"])
    logging.info("validated {} JSON files".format(i+1))

if __name__ == '__main__':
    main()
