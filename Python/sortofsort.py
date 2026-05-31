n = int(input())

og = [int(x) for x in input().split()]
sortof = [og[0]]

for i in range(1, len(og)):
    if og[i] >= sortof[-1]:
        sortof.append(og[i])

print(*sortof)
