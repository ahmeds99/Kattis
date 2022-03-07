import sys

info = sys.stdin.readline().split()

antMålinger = int(info[0])
variasjon = int(info[1])

målinger = sys.stdin.readline().split()

dagMedMestVariasjon = 1
mestVariasjon = int(målinger[0])

dagMedMinstVariasjon = 1
minstVariasjon = int(målinger[0])

for i in range(1, len(målinger) + 1):
    måling = int(målinger[i - 1])

    størsteForskjellStørst = abs(måling - mestVariasjon) - variasjon * abs(i - dagMedMestVariasjon)
    størstForskjellMinst = abs(måling - minstVariasjon - variasjon * abs(i - dagMedMinstVariasjon))
    print("størst:", størsteForskjellStørst)
    print("minst:", størstForskjellMinst, "\n")

    print("dag med minst variasjon", dagMedMinstVariasjon)
    print("minst variasjon:", minstVariasjon)


    if størsteForskjellStørst >= størstForskjellMinst:
        if måling > mestVariasjon:
            dagMedMestVariasjon = i
            mestVariasjon = måling

        # print(størsteForskjellStørst, end=" ")
    else:
        if måling <= minstVariasjon:
            dagMedMinstVariasjon = i
            minstVariasjon = måling
        # print(størstForskjellMinst, end=" ")
    
    