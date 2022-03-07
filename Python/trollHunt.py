fil = open("trollhunt.txt")

for linje in fil:
    biter = linje.split()
    broer = int(biter[0]) - 1
    riddere = int(biter[1])
    ridderePerGruppe = int(biter[2])

broerPerDag = int(riddere / ridderePerGruppe)
if (broer % broerPerDag == 0):
    print(int(broer / broerPerDag))
else:
    print(int(broer / broerPerDag) + 1)