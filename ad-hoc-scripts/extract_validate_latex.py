#! /usr/bin/env python3

from __future__ import print_function

import os
import sys
import json
import tempfile
import subprocess

filepath = sys.argv[1]
filename = os.path.basename(filepath)
equajson = json.load(open(filepath))

try:
    latex_documents = equajson["markup-languages"]["LaTeX"]
except KeyError:
    # If there isn't any LaTeX markup, there is nothing to validate.
    sys.exit(0)

for document in latex_documents:
    try:
        latex = document["markup"]
    except KeyError:
        sys.stdout.write("Missing LaTeX markup in file `{}'".format(filepath))
    fp = tempfile.NamedTemporaryFile(mode='w')
    fp.file.write(latex)
    fp.file.flush()
    try:
        subprocess.check_output(['pdflatex', '-halt-on-error', fp.name], stderr=subprocess.STDOUT, cwd=tempfile.gettempdir())
    except subprocess.CalledProcessError as latex_err:
        sys.stderr.write(latex_err.output.decode())
        raise
    finally:
        fp.close()
