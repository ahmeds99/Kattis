# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C):
    oversikt = {}
    oversikt["a"] = A 
    oversikt["b"] = B
    oversikt["c"] = C

    resultat = ""
    while True:
        oversikt = dict(sorted(oversikt.items(), key=lambda elem: elem[1], reverse=True))
        nøkler = list(oversikt)
        størstFrek = nøkler[0]

        if oversikt[størstFrek] == 0:
            break 
        if len(resultat) >= 2 and resultat[-2:] == størstFrek + størstFrek:
            størstFrek = nøkler[1]
            if oversikt[størstFrek] == 0:
                break
        oversikt[størstFrek] -= 1
        resultat += størstFrek
    print(resultat)
solution(6, 1, 1)