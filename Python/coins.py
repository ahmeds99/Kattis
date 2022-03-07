import sys

antallMynter = info = int(sys.stdin.readline())

if antallMynter - 1 % 4 == 0:
    print(2, flush=True)
    antallMynter -= 2
elif antallMynter > 2:
    print(3, flush=True)
    antallMynter -= 3
else:
    print(1, flush=True)
    antallMynter -= 1

info = sys.stdin.readline().strip()

while antallMynter > 0 and info != "I give up\n":
    antallMynter -= int(info)
    if antallMynter % 2 != 0:
        print(2, flush=True)
        antallMynter -= 2
    elif antallMynter > 2:
        print(3, flush=True)
        antallMynter -= 3
    else:
        print(1, flush=True)
        antallMynter -= 1

    info = sys.stdin.readline()

exit(0)