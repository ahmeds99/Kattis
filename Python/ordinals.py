import sys


def ordinals(n):
    l = []
    if n <= 0:
        return l

    for i in range(n):
        l.append(ordinals(i))
    return l


svar = (
    ordinals(int(sys.stdin.readline()))
    .__str__()
    .replace("[", "{")
    .replace("]", "}")
    .replace(", ", ",")
)
print(svar)
