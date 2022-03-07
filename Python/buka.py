import sys

a = int(sys.stdin.readline())
operand = sys.stdin.readline().strip()
b = int(sys.stdin.readline())

if operand == "+":
    print(a + b)
else:
    print(a * b)