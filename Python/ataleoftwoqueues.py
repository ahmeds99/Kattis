info = input()

first = sum([int(x) for x in input().split()])
second = sum([int(x) for x in input().split()])

if first < second:
    print("left")
elif second < first:
    print("right")
else:
    print("either")
