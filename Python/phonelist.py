n = int(input())

for _ in range(n):
    n_numbers = int(input())

    oversikt = []
    gyldig = True
    for _ in range(n_numbers):
        num = input()
        if gyldig:
            for nr in oversikt:
                if num.startswith(nr):
                    gyldig = False
                    break

            oversikt.append(num)

    print("YES" if gyldig else "NO")
