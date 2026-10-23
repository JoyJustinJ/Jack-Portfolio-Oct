with open('jack_app_code.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Let's search for arrays or lists of projects, skills, etc.
# Print chunks with curly braces or arrays
print("Length:", len(text))

# Let's write a small script to find all text strings
strings = re.findall(r'"([^"]+)"', text)
for s in strings:
    if len(s) > 15:
        print("-", s)
