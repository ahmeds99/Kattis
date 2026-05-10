longest_streak = 0
streak = False
cur = 0
for _ in range(int(input())):
    my, opps = [int(x) for x in input().split()]

    if opps >= my:
        streak = False
        cur = 0
        continue

    cur += 1
    if cur > longest_streak:
        longest_streak = cur

print(longest_streak)
