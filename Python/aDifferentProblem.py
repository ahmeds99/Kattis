fil = open("diffProb.txt")

for linje in fil:
    biter = linje.split()
    tallEn = int(biter[0])
    tallTo = int(biter[1])
    
    print(abs(tallEn - tallTo))