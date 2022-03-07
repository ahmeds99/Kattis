import sys, math

info = sys.stdin.readline().split()

kariStart = (int(info[0]), int(info[1]))
olaStart = (int(info[2]), int(info[3]))

kariSlutt = (int(info[4]), int(info[5]))
olaSlutt = (int(info[6]), int(info[7]))


k1 = abs(kariStart[0] - olaStart[0])
k2 = abs(kariStart[1] - olaStart[1])

startHyp = math.sqrt((k1 ** 2) + (k2 ** 2))

o1 = abs(kariSlutt[0] - olaSlutt[0])
o2 = abs(olaSlutt[1] - kariSlutt[1])

olaHyp = math.sqrt((o1 ** 2) + (o2 ** 2))

print(max(startHyp, olaHyp))
