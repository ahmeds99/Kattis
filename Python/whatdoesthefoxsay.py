n = int(input())

while n > 0:
    recording = input().strip().split()
    words_by_other = set()

    info = input().strip()

    while info != "what does the fox say?":
        words_by_other.add(info.split()[2])
        info = input().strip()

    print(*list(filter(lambda x: x not in words_by_other, recording)))

    n -= 1
