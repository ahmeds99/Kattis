import sys 

ordet = sys.stdin.readline().strip()

if ordet[:2] == "he" and ordet[-2:] == "ey":
    antE = ordet.count("e")
    nyttOrd = ordet[:1]
    for i in range(antE * 2):
        nyttOrd += "e"
    nyttOrd += ordet[-1:]
    print(nyttOrd)