#! /usr/bin/env python3

import sys
import json

for arg in sys.argv[1:]:
    with open(arg) as f:
        equajson = json.load(f)

    try:
        latex = equajson["markup-languages"]["LaTeX"][0]["markup"]
    except KeyError:
        continue

    if 'documentclass' not in latex:
        with_boilerplate = "\\documentclass{article}\n\\begin{document}\n\\[\n%s\n\\]\n\\end{document}" % latex
        equajson["markup-languages"]["LaTeX"][0]["markup"] = with_boilerplate

    with open(arg, 'w') as f:
        json.dump(equajson, f, indent=4, separators=(',', ': '), ensure_ascii=False, sort_keys=True)
