info = input().strip()

truls, henry = 0, 0

for letter in info:
    if letter == "T":
        truls += 1
    else:
        henry += 1

    if (truls >= 11 or henry >= 11) and abs(truls - henry) > 1:
        truls = 0
        henry = 0


print(f"{truls}-{henry}")
