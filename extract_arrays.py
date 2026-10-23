with open('jack_bundle.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find position of function V3
pos = text.find('function V3(')
print("V3 position:", pos)
if pos != -1:
    before_v3 = text[max(0, pos-8000):pos]
    with open('jack_data_definitions.js', 'w', encoding='utf-8') as out:
        out.write(before_v3)
    print("Wrote jack_data_definitions.js, length:", len(before_v3))
