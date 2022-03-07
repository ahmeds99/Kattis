import collections

fil = open("notAmused.txt")

dagNr = 1
for linje in fil:
    biter = linje.split()

    if biter[0] == "OPEN":
        if dagNr > 1:
            print()

        print(f"Day {dagNr}")
        dagNr += 1
        oversikt = {}

    elif biter[0] == "CLOSE":
        sortert = collections.OrderedDict(sorted(oversikt.items()))
        for navn, kostnad in sortert.items():
            print(f"{navn} ${round((abs(kostnad) * 0.1), 2)}0")
    
    elif biter[0] == "ENTER":
        if biter[1] in oversikt:
            oversikt[biter[1]] += int(biter[2])
        else:
            oversikt[biter[1]] = int(biter[2])

    else:
        oversikt[biter[1]] -= int(biter[2])