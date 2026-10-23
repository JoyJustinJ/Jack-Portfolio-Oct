import re
import json

with open('jack_bundle.js', 'r', encoding='utf-8') as f:
    code = f.read()

print("File size:", len(code))

# Find strings
strings = re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"', code)
print(f"Total strings found: {len(strings)}")

interesting = []
for s in strings:
    s_clean = s.strip()
    if len(s_clean) > 3 and any(w in s_clean.lower() for w in [
        'jack', 'gilbert', 'developer', 'engineer', 'education', 'project', 
        'experience', 'skill', 'b.tech', 'college', 'school', 'github', 
        'linkedin', 'gmail', 'mail', 'phone', 'react', 'python', 'about', 'summary'
    ]):
        if s_clean not in interesting:
            interesting.append(s_clean)

with open('jack_extracted.txt', 'w', encoding='utf-8') as out:
    for item in interesting:
        out.write(item + '\n')

print(f"Wrote {len(interesting)} interesting strings to jack_extracted.txt")
