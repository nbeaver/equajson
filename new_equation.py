#! /usr/bin/env python3
from __future__ import print_function

import datetime
import os
import sys
import json
import uuid
import argparse
import logging

def get_year():
    now = datetime.datetime.now()
    return now.year

def get_iso_date():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d')

def get_username():
    try:
        # POSIX only
        import pwd
        gecos_field =  pwd.getpwuid(os.getuid()).pw_gecos
        full_name = gecos_field.split(',')[0]
        return full_name
    except ImportError:
        import getpass
        return getpass.getuser()

def main():
    parser = argparse.ArgumentParser(
        description='Create new equajson file.')
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
    # TODO: pass argument for equation.
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    new_uuid = str(uuid.uuid4())

    equajson = \
    {
        "copying": {
            "authors": [
                get_username()
            ],
            "license-name": "MIT (Expat) License",
            "license-url": "http://opensource.org/licenses/MIT",
            "year": get_year(),
        },
        "description": {
            "verbose": "<FIXME>",
            "terse": "<FIXME>",
        },
        "markup-languages": {
            "LaTeX": [
                {
                    "markup": "<FIXME>",
                }
            ]
        },
        "relevant-urls": [
            {
                "date-known-good": get_iso_date(),
                "url": "<FIXME>",
            }
        ],
        "unicode-pretty-print": {
            "multiline": [
                "<FIXME>",
                "<FIXME>",
                "<FIXME>",
            ],
            "terms": [
                {
                    "classification": {
                        "always-an-integer": False,
                        "always-dimensionless": False,
                        "always-positive": False,
                        "always-scalar": False,
                        "bound-variable": False,
                        "fixed-constant": False,
                        "special-function": False,
                    },
                    "label": "<FIXME>",
                    "symbol": "<FIXME>",
                    "urls": [
                        "<FIXME>",
                    ]
                },
                {
                    "classification": {
                        "always-dimensionless": False,
                        "fixed-constant": False,
                    },
                    "label": "<FIXME>",
                    "symbol": "<FIXME>",
                    "urls": [
                        "<FIXME>",
                    ]
                }
            ]
        },
        "uuid": new_uuid,
    }

    root = sys.path[0]
    new_filename = new_uuid + '.json'
    new_filepath = os.path.join(root, 'json', new_filename)
    with open(new_filepath, 'w') as new_file:
        json.dump(equajson, new_file, indent=4, separators=(',', ': '), sort_keys=True)
        print('Created new equation:\n{}'.format(new_filepath))

if __name__ == '__main__':
    main()
