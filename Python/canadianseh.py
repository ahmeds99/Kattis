import sys

inp = sys.stdin.readline().strip()
is_canadian = len(inp) > 2 and inp[-3:] == "eh?"
print("Canadian!" if is_canadian else "Imposter!")
