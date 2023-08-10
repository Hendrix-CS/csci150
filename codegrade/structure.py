# CodeGrade Semgrep Structure Check Script to be used for Autotest V2
#
# Usage:
# - In a "Script" block move uploaded script to student directory using:
#   "mv $UPLOADED_FILES/structure.py ."
# - Create an IO Test block and run this script in that:
#   "python3 structure.py <LANGUAGE> <STUDENTSCRIPT>"
# - Create one or more Simple Match blocks with as input semgrep patterns:
#   "pattern: import numpy"

import os
import sys
import subprocess

if len(sys.argv) < 2:
    print("Usage: python3 structure.py <student file>")
    sys.exit(1)

language = os.path.splitext(sys.argv[1])[1][1:]

starts = False
indent = '  '
pattern = ''
for line in sys.stdin:
    if not starts and not line.startswith('pattern'):
        pattern += '  pattern: |\n'
        indent += '  '
        starts = True
    else:
        starts = True

    pattern += indent + line

if not pattern.startswith('  pattern'):
    pattern = '  pattern: ' + pattern[2:]

yaml = f"""
rules:
- id: RuleID
{pattern}
  message: message
  languages: [{language}]
  severity: INFO
"""

with open('rule.yml', 'w') as f:
    f.write(yaml)

process = subprocess.run(
    ["semgrep",
    "--error",
    "--config",
    'rule.yml',
    "--no-rewrite-rule-ids",
    '--disable-version-check',
    '--timeout',
    '0',
    '--disable-nosem',
    sys.argv[1]], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if process.returncode == 0:
    print("Not found!")
    exit(0)
elif process.returncode == 1:
    print("Found!")
    exit(0)
elif process.returncode == 2:
    print("File not found: " + sys.argv[1])
    exit(1)
 