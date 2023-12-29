_, k = [int(x) for x in input().split()]

print(
    *[
        x
        for _, x in list(
            filter(lambda e: (e[0] + 1) % k == 0, enumerate(input().split()))
        )
    ]
)
