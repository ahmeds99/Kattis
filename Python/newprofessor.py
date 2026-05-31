import bisect

colors = int(input())

days = 0
oversikt = []

for i in range(colors):
    bisect.insort(oversikt, int(input()), key=lambda x: -x)

if colors < 5:
    print(colors)

else:
    full_week_run = False
    while len(oversikt) >= 5:
        oversikt.sort(reverse=True)

        days_on_this_iteration = 0
        full_week_run = False
        for i in range(len(oversikt)):
            if oversikt[i] > 0:
                days_on_this_iteration += 1
                oversikt[i] = oversikt[i] - 1

            if days_on_this_iteration == 5:
                full_week_run = True
                break

        days += days_on_this_iteration
        for i in range(len(oversikt)):
            if i < len(oversikt) and oversikt[i] <= 0:
                oversikt.pop(i)

    oversikt.sort(reverse=True)

    if full_week_run:
        i = 0
        while i < len(oversikt) and oversikt[i] > 0:
            days += 1
            i += 1

    print(days)
