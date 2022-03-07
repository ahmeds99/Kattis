import sys

bites = int(sys.stdin.readline())
liste = sys.stdin.readline().split()

nesteTall = 1
fishy = False
for i in range(1, bites + 1):
    if liste[i - 1].isnumeric() and int(liste[i - 1]) != i:
        # print(liste[i-1], i)
        fishy = True

if fishy:
    print("something is fishy")
else:
    print("makes sense")