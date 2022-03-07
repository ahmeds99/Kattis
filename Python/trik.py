import sys

trekk = sys.stdin.readline().strip()
ball = 1
forsteTrekk = True
for t in trekk:
    if forsteTrekk:
        if t == "A":
            ball = 2
        else:
            ball = 3
        forsteTrekk = False

    else:
        if t == "A":
            if ball == 2:
                ball = 1
            elif ball == 1:
                ball = 2
        elif t == "B":
            if ball == 2:
                ball = 3
            elif ball == 3:
                ball = 2
        else:
            if ball == 3:
                ball = 1
            elif ball == 1:
                ball = 3

print(ball)
