import re

with open('data/witcher_raw.txt', 'r') as f:
    text_raw = f.read()

text = text_raw.replace('\n', ' ').replace('Edit', ' ')
brackets_substrings = re.findall(r'\[.*?\]', text)
for substring in brackets_substrings:
    text = text.replace(substring, '')

with open('data/witcher.txt', 'w') as f:
    f.write(text)
