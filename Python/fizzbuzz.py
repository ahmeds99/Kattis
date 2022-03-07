import sys

info = sys.stdin.readline().split()

førsteDivisor = int(info[0])
andreDivisor = int(info[1])
antallTall = int(info[2])

for i in range(1, antallTall + 1):
    if i % førsteDivisor == 0:
        if i % andreDivisor == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i % andreDivisor == 0:
        print("Buzz")
    else:
        print(i)