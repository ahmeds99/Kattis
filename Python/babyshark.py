words = input().strip().split()

longest = words[0]
streak = 1

prev = words[0]
curr_streak = 1
for i in range(len(words) - 1):
    if words[i + 1] == prev:
        curr_streak += 1
    else:
        prev = words[i + 1]
        curr_streak = 1

    if curr_streak > streak:
        longest = prev
        streak = curr_streak

print(longest)
