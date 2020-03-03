import string

text = input("Word = ")
text = list(text.lower())
text_line = len(text)
alphabet = string.ascii_lowercase
line = len(alphabet)
for t in range(len(text)):
    for i in range(line):
        if text[t] == alphabet[i]:
            text[t] = alphabet[(i + text_line) % line]
            break

print(text)

for t in range(len(text)):
    for i in range(line):
        if text[t] == alphabet[i]:
            text[t] = alphabet[(i - text_line) % line]
            break

print(text)

