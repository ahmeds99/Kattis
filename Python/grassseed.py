cost = float(input())
total_cost = 0.0

for line in range(int(input())):
    len, wid = [float(x) for x in input().split()]
    total_cost += len * wid * cost

print(total_cost)
