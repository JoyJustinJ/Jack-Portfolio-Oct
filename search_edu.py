with open('jack_bundle.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Look for degree, university, stats, location
for term in ['degree', 'b.tech', 'b.e', 'engineering', 'karunya', 'krishnagiri', 'university', 'college', 'cgpa', 'gpa', 'matriculation', 'school']:
    matches = [m.start() for m in re.finditer(term, text, re.IGNORECASE)]
    print(f"Term '{term}': {len(matches)} matches")
    for pos in matches[:3]:
        print("  Snippet:", text[max(0, pos-100):min(len(text), pos+150)])
