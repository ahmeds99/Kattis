import sys
import math

for linje in sys.stdin:
    tall = int(linje)
    total = 1
    for i in range(2, int(math.sqrt(tall)) + 1):
        if tall % i == 0:
            total += i
            if i*i != tall:
                total += tall // i


    if total == tall:
        print(f"{tall} perfect")
    elif total >= tall - 2 and total <= tall + 2:
        print(f"{tall} almost perfect")
    else:
        print(f"{tall} not perfect")