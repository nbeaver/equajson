#! /usr/bin/env python
import json
import jsonschema
import sys
import os

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
    num_args = len(sys.argv) - 1
    if num_args != 2:
        sys.stderr.write("Usage: python "+sys.argv[0]+" equajson.json schema.json"+'\n')
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
