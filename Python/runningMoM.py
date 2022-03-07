import sys

def DFS(G, s, visited):
    visited[s] = s
    for nabo in G[s]:
        if nabo in visited:
            return True
        visited[nabo] = nabo
        verdi = DFS(G, nabo, visited)
        if verdi:
            return True 

        visited.pop(nabo)
        
    return False

graf = {}
antKanter = int(sys.stdin.readline())
for i in range(antKanter):
    info = sys.stdin.readline().split()
    node = info[0]
    nabo = info[1]

    if nabo not in graf:
        graf[nabo] = []

    if node in graf:
        graf[node].append(nabo)
    else:
        graf[node] = [nabo]

for linje in sys.stdin:
    by = linje.strip()
    funnet = DFS(graf, by, {})
    if funnet:
        print(by, "safe")
    else:
        print(by, "trapped")