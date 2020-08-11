#! /usr/bin/env python3
from __future__ import print_function
import os
import sys
import json
import argparse
import logging

def pretty_print(equation):
    print(equation["description"]["terse"])
    eqn_dict = equation["unicode-pretty-print"]
    equation_text = eqn_dict["multiline"]
    for line in equation_text:
        print(line)
    if "terms" in eqn_dict:
        print("where:")
        for param_dict in eqn_dict["terms"]:
            symbol = param_dict["symbol"]
            label = param_dict["label"]
            print(symbol,'=',label)

def print_markup(equation, markup_language):
    for representation in equation["markup-languages"][markup_language]:
        markup = representation['markup']
        print(markup)


def main():
    parser = argparse.ArgumentParser(
        description='Search for equations.')
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
    parser.add_argument(
        'query', help='Search string to match.')
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)
    here = sys.path[0]
    json_dir = os.path.join(here, 'json')

    for filename in os.listdir(json_dir):
        if not filename.endswith('.json'):
            continue
        filepath = os.path.join(json_dir, filename)
        with open(filepath) as json_file:
            try:
                equation = json.load(json_file)
            except ValueError:
                logging.warning("Invalid JSON for file: `{}'\n".format(json_file.name))
                continue # try the next file
            description = equation["description"]["verbose"]
            if args.query.lower() in description.lower():
                pretty_print(equation)
                #print_markup(equation, 'LaTeX')
                print(filepath)
                print('-'*80)
        # TODO: exit with error if no results are found.

if __name__ == '__main__':
    main()
