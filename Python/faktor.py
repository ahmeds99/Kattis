import sys 

info = sys.stdin.readline().split()

antArtikler = int(info[0])
faktor = float(info[1]) - 0.9999999

print(int(antArtikler * faktor) + 1)
