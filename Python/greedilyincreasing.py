num = int(input())

info = [int(x) for x in input().strip().split()]
result = [info[0]]

for i in range(len(info) - 1):
    if info[i + 1] > info[i] and info[i + 1] > result[-1]:
        result.append(info[i + 1])

print(len(result))
print(*result)
