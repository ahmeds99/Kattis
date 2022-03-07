import sys 

stackÅpen = []
antChar = int(sys.stdin.readline())

info = sys.stdin.readline()
indeks = 0
fantFeil = False
for char in info:
    if char == "(" or char == "[" or char == "{":
        stackÅpen.append(char)
    elif char == ")" or char == "]" or char == "}":
        if not stackÅpen:
            print(char, indeks)
            fantFeil = True
            break
        motsatt = stackÅpen.pop()
        if char == ")" and motsatt != "(":
            print(char, indeks)
            fantFeil = True
            break
        elif char == "]" and motsatt != "[":
            print(char, indeks)
            fantFeil = True
            break
        elif char == "}" and motsatt != "{":
            print(char, indeks)
            fantFeil = True
            break
    
    indeks += 1

if not fantFeil:
    print("ok so far")