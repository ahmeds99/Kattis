inp = input()

length = len(inp)
num_whitespace = 0
lower = 0
upper = 0
symbols = 0


for letter in inp:
    if letter == "_":
        num_whitespace += 1
    elif letter.islower():
        lower += 1
    elif letter.isupper():
        upper += 1
    else:
        symbols += 1

print(num_whitespace / length)
print(lower / length)
print(upper / length)
print(symbols / length)
