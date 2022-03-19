import sys

antTall = sys.stdin.readline()

sum = 1
for tall in sys.stdin.readline().split():
    sum += int(tall)

print(sum % 3)