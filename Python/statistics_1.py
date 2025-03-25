import sys

caseNr = 1
for linje in sys.stdin:
    case = linje.split()
    min = 1_000_001
    max = -1_000_001
    for t in case[1:]:
        tall = int(t)
        if tall < min:
            min = tall
        if tall > max:
            max = tall
    
    print(f"Case {caseNr}: {min} {max} {max - min}")
    caseNr += 1