import string

text = input("Word = ")
text = list(text.lower())
alphabet = string.ascii_lowercase
line = len(alphabet)
for t in range(len(text)):
    for i in range(line):
        if text[t] == alphabet[i]:
            text[t] = alphabet[line - i - 1]
            break

print(text)

for t in range(len(text)):
    for i in range(line):
        if text[t] == alphabet[i]:
            text[t] = alphabet[line - i - 1]
            break

print(text)
