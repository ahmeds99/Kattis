import sys

nedreGrense = 0
øvreGrense = 11

nåværendeTall = int(sys.stdin.readline())

while nåværendeTall != 0:
    forrigeTall = nåværendeTall
    respons = sys.stdin.readline().strip()
    if respons == "right on":
        if nedreGrense < forrigeTall < øvreGrense:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        
        nedreGrense = 0
        øvreGrense = 11
    
    elif respons == "too low":
        nedreGrense = max(forrigeTall, nedreGrense)

    else:
        øvreGrense = min(forrigeTall, øvreGrense)
    
    nåværendeTall = int(sys.stdin.readline())

