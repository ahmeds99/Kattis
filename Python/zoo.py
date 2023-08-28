import sys
from collections import defaultdict

ant_linjer = int(sys.stdin.readline())
ant_caser = 1

while ant_linjer != 0:
    oversikt = {}
    for i in range(ant_linjer):
        animal_type = sys.stdin.readline().strip().split(" ")[-1].lower()
        oversikt[animal_type] = (
            1 if animal_type not in oversikt else oversikt[animal_type] + 1
        )

    sortert = sorted(oversikt.items())
    print(f"List {ant_caser}:")
    [print(f"{name} | {ant}") for (name, ant) in sortert]
    ant_caser += 1
    ant_linjer = int(sys.stdin.readline())
