import sys

oversikt = {}
teller = 0

for i in range(int(sys.stdin.readline())):
    ord = sys.stdin.readline().replace("-", " ").lower()
    if ord not in oversikt:
        oversikt[ord] = ord
        teller += 1

print(teller)