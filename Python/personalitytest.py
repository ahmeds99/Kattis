from collections import Counter

leaders = {"1": "leader", "2": "intellectual", "3": "social", "4": "practical"}

for _ in range(int(input())):
    c = Counter(input().split())
    print(leaders[c.most_common(1)[0][0]])
