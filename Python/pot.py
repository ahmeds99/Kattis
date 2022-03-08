import sys 

antTall = int(sys.stdin.readline())
total = 0

for i in range(antTall):
    tallet = sys.stdin.readline()
    total += int(tallet[:-2]) ** int(tallet[-2])

print(total)