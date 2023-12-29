tekst = input().split()
print("yes" if len(tekst) == len(set(tekst)) else "no")
