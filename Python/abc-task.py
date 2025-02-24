inp = sorted([int(x) for x in input().split()])
mappings = list(input())
num_mappings = {"A": inp[0], "B": inp[1], "C": inp[2]}

[print(num_mappings[x], end=" ") for x in mappings]
