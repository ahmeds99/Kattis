import sys 

indeks = 0
ordet = sys.stdin.readline()
for bokstav in ordet:
    if (bokstav.lower() == "a"):
        print(ordet[indeks:])
        break
    else:
        indeks += 1
