import sys
import bisect

oversikt = []

for i in range(5):
    linje = sys.stdin.readline().strip()
    if "FBI" in linje:
        bisect.insort_right(oversikt, i + 1)

if len(oversikt) == 0:
    print("HE GOT AWAY!")
else:
    print(*oversikt)
