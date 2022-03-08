import sys

linje = sys.stdin.readline().split()

if (linje[0] == "OCT" and linje[1] == "31") or (linje[0] == "DEC" and linje[1] == "25"):
    print("yup")
else:
    print("nope")