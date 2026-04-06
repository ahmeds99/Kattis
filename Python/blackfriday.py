n = int(input())

case = input().split()
oversikt = {}
for i in range(len(case)):
    dice = case[i]
    if dice in oversikt:
        oversikt[dice] = -1
    else:
        oversikt[dice] = i

found = False
for i in range(6, 0, -1):
    if str(i) in oversikt and oversikt[str(i)] != -1:
        print(oversikt[str(i)] + 1)
        found = True
        break

if not found:
    print("none")
