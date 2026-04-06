n = int(input())

oversikt = {}

for i in range(n):
    case = input().strip().split()[1:]

    for app in case:
        if app not in oversikt:
            oversikt[app] = ""
            break

print(*oversikt.keys())
