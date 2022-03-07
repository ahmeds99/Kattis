import sys

info = sys.stdin.readline().split()
antall = int(info[0])
avhengigheter = {}

for i in range(int(info[1])):
    deler = sys.stdin.readline().split()
    avhengigheter[deler[0]] = deler[1]

if len(avhengigheter) != antall - 1:
    print("IMPOSSIBLE")
else:
    tall = "1"
    while tall in avhengigheter:
        print(tall)
        tall = avhengigheter[tall]
    print(tall)