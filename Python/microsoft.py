# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    allChars = {}
    validChars = []
    for c in S:
        kopi = c
        if c.islower() and kopi.upper() in allChars:
            if c.upper() not in validChars:
                validChars.append(c.upper())

        elif c.isupper() and kopi.lower() in allChars:
            if c.upper() not in validChars:
                validChars.append(c.upper())

        allChars[c] = c
    print(validChars)
    if len(validChars) == 0:
        return "NO"
    else:
        største = ""
        for validC in validChars:
            if validC > største:
                største = validC
        
        return største
