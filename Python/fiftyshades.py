import sys

num_lines = int(sys.stdin.readline().strip())
total = 0

for i in range(num_lines):
    line = sys.stdin.readline().strip().lower()

    if "rose" in line or "pink" in line:
        total += 1

if total == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(total)
