import math
import sys

ant_caser = int(sys.stdin.readline())
calories_per_bottle = 400

for _ in range(ant_caser):
    print(math.ceil(int(sys.stdin.readline()) / calories_per_bottle))