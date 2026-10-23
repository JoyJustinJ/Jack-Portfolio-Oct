import re

with open('jack_bundle.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Find strings of length > 15 that don't look like code or minified vars
# Or search around "Jack"
jack_pos = [m.start() for m in re.finditer(r'jack', text, re.IGNORECASE)]
print(f"Occurrences of 'jack': {len(jack_pos)}")

for idx, pos in enumerate(jack_pos):
    snippet = text[max(0, pos-200):min(len(text), pos+300)]
    print(f"\n--- Occurrence {idx+1} (at {pos}) ---")
    print(snippet)
