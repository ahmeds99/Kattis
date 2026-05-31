words = input().split()

new = []
for word in words:
    isString = False
    isDigit = False
    for c in word:
        if c.isdigit():
            isDigit = True
        if c.isalpha():
            isString = True

    if isString and isDigit:
        new.append("*" * len(word))
    else:
        new.append(word)

print(*new)
