import string
import random

prime_numbers = []

for i in range(2, 200):
    check = 0
    for j in range(1, i + 1):
        if i % j == 0:
            check += 1
    if check == 2:
        prime_numbers.append(i)

p = random.choice(prime_numbers)
q = random.choice(prime_numbers)
n = p * q
d = random.choice(prime_numbers)
f = (p - 1) * (q - 1)
e = 0
for i in range(2, 50000):
    if (i * d) % f == 1:
        e = i
        break

text = input("Word = ")
text = list(text.lower())
text_line = len(text)
alphabet = string.ascii_lowercase
line = len(alphabet)

print('{e = %s, n = %s}' % (e, n))
for t in range(len(text)):
    for i in range(line):
        if text[t] == alphabet[i]:
            text[t] = (i + 1) ** e % n
            break

print(text)

print('{d = %s, n = %s}' % (d, n))

for t in range(len(text)):
    text[t] = int(text[t]) ** d % n
    text[t] = alphabet[text[t] - 1]

print(text)
