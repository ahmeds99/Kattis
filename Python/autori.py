import sys

linje = sys.stdin.readline().split("-")
shortVariation = ""

for ord in linje:
    shortVariation += ord[0]

print(shortVariation)

