import string

text = input("Word = ")
key = int(input("Input bias "))
text = list(text.lower())
alphabet = string.ascii_lowercase
line = len(alphabet)
for t in range(len(text)):
    for i in range(line):
        if text[t] == alphabet[i]:
            text[t] = alphabet[(i + key)%line]
            break

print(text)

for t in range(len(text)):
    for i in range(line):
        if text[t] == alphabet[i]:
            text[t] = alphabet[(i - key)%line]
            break

print(text)
