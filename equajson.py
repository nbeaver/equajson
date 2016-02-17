#! /usr/bin/env python
from __future__ import print_function
import os
import sys
import json

def pretty_print(equation):
    print(equation["description"]["terse"])
    eqn_dict = equation["unicode-pretty-print"]
    equation_text = eqn_dict["multiline"]
    for line in equation_text:
        print(line)
    if "parameters" in eqn_dict:
        print("where:")
        for param_dict in eqn_dict["parameters"]:
            symbol = param_dict["symbol"]
            label = param_dict["label"]
            print(symbol,'=',label)


def main(query):
    here = sys.path[0]
    json_dir = os.path.join(here, 'equajson')

    for filename in os.listdir(json_dir):
        if not filename.endswith('.json'):
            continue
        filepath = os.path.join(json_dir, filename)
        with open(filepath) as json_file:
            try:
                equation = json.load(json_file)
            except ValueError:
                sys.stderr.write("Invalid JSON for file: `{}'\n".format(json_file.name))
                continue # try the next file
            description = equation["description"]["verbose"]
            if query.lower() in description.lower():
                pretty_print(equation)
                print('-'*80)


if __name__ == '__main__':
    num_args = len(sys.argv) - 1
    if num_args != 1:
        sys.stderr.write("Usage: python "+sys.argv[0]+" query"+'\n')
        sys.exit(1)
    main(sys.argv[1])
