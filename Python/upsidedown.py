n = input()
print(*sorted([x[::-1] for x in input().split()], reverse=True))
