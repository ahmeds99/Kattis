seats, groups = [int(x) for x in input().split()]

notAccepted = 0
for g in [int(x) for x in input().split()]:
    if seats - g >= 0:
        seats -= g
    else:
        notAccepted += 1

print(notAccepted)
