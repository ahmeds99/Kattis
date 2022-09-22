import sys

antCaser = int(sys.stdin.readline())

for _ in range(antCaser):
    total = 0
    tall1 = sys.stdin.readline().strip().replace(" ", "")
    tall2 = sys.stdin.readline().strip().replace(" ", "")

    total = int(tall1) + int(tall2)
    print(" ".join(str(total)))