#! /usr/bin/env python3

import sys
import json

with open(sys.argv[1]) as f:
    equajson = json.load(f)

field_list = [
    "always-an-integer",
    "always-positive",
    "always-dimensionless",
    "bound-variable",
    "fixed-constant",
    "special-function"
]
for term in equajson["unicode-pretty-print"]["terms"]:
    print(term)
    if any(x in field_list for x in term.keys()):
        term["classification"] = {}
        del_list = []
        for field in term.keys():
            print(field)
            if field in field_list:
                term["classification"][field] = term[field]
                del_list.append(field)
        for field in del_list:
            del term[field]

with open(sys.argv[1], 'w') as f:
    json.dump(equajson, f, indent=4, separators=(',', ': '), ensure_ascii=False, sort_keys=True)