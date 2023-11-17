'''Read tasks from a variety of possible sources.

If a single argument is passed to the program beginning with 'http://', it will
read tasks from that URL. Otherwise it will read from files passed as
parameters. Otherwise it will read from stdin.
'''

import os
import subprocess
import sys
import fileinput

def Tasks():
  if len(sys.argv) > 1 and sys.argv[1].startswith('http://'):
    assert len(sys.argv) == 2, 'Cannot read tasks from both argv and http'
    url = sys.argv[1]
    try:
      while True:
        yield subprocess.check_output(['curl', '--silent', url]).strip()
    except subprocess.CalledProcessError:
      # Done, we hope!
      pass
  else:
    yield from fileinput.input()
