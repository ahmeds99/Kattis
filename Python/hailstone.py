def hailstone(n, total):
    total += [n]
    if n == 1:
        return total
    elif n % 2 == 0:
        return hailstone(n / 2, total)
    else:
        return hailstone(3 * n + 1, total)


print(len(hailstone(int(input()), [])))
