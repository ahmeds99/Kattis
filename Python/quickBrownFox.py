import sys

antCaser = int(sys.stdin.readline())
for i in range(antCaser):
    base = "abcdefghijklmnopqrstuvwxyz"
    for c in sys.stdin.readline():
        if c.lower() in base:
            base = base.replace(c.lower(), "")
    
    if base == "": print("pangram")
    else: print("missing", base)
