from collections import defaultdict
import functools

tekst = input()

oversikt = {"T": 0, "C": 0, "G": 0}

for c in tekst:
    oversikt[c] += 1

unike_sett = 7 * min(oversikt.values())
print(
    functools.reduce(lambda acc, en: acc + en**2, oversikt.values(), 0) + unike_sett
)
