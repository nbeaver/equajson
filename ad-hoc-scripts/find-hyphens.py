#! /usr/bin/env python

from __future__ import print_function

import sys
import json

for arg in sys.argv[1:]:
    with open(arg) as f:
        equajson = json.load(f)

    lines = equajson["unicode-pretty-print"]["multiline"]

    if any(['-' in line for line in lines]):
        print(arg)
