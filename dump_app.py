with open('jack_bundle.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the component code between 330000 and 347000
start = 330000
end = len(text)
section = text[start:end]

with open('jack_app_code.txt', 'w', encoding='utf-8') as f:
    f.write(section)

print("Wrote jack_app_code.txt, length:", len(section))
