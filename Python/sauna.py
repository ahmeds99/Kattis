n = int(input())

minste = 0
maks = float("inf")

bad_news = False
for n in range(n):
    lav, hoy = [int(x) for x in input().split()]

    if lav > maks or hoy < minste:
        bad_news = True
        break

    if lav > minste:
        minste = lav

    if hoy < maks:
        maks = hoy

if bad_news:
    print("bad news")

else:
    print(maks - minste + 1, minste)
