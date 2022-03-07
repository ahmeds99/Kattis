
fil = open("votes.txt")

antallTester = int(fil.readline())
for i in range(antallTester):
    antKandidater = int(fil.readline())
    antallStemmer = 0
    oversikt = []
    for j in range(antKandidater):
        stemmer = int(fil.readline())
        antallStemmer += stemmer
        oversikt.append(stemmer)

    majoritet = antallStemmer / 2
    major = False
    minor = False

    foreløpigLeder = 0
    foreløpigFlest = 0
    toPåTopp = False

    for k in range(len(oversikt)):
        if not major and oversikt[k] > majoritet:
            print("majority winner ", k + 1)
            major = True
        elif oversikt[k] > foreløpigFlest:
            if k != 0 and oversikt[k] != oversikt[0]:
                minor = True
            elif len(oversikt) > 1 and oversikt[0] > oversikt[1]:
                minor = True

            foreløpigFlest = oversikt[k]
            foreløpigLeder = k
            toPåTopp = False
        elif oversikt[k] == foreløpigFlest:
            toPåTopp = True
            minor = False
        
    if not minor and not major:
        print("no winner")
    elif not major and not toPåTopp:
        print("minority winner ", foreløpigLeder + 1)