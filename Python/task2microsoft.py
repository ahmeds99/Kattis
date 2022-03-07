# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    tallListe = []
    if N % 2 == 1:
        tallListe.append(0)
    for i in range(1, N // 2  + 1):
        tallListe.append(i)
        tallListe.append(-i)
    
    print(tallListe)
    print(sum(tallListe))

solution(14)