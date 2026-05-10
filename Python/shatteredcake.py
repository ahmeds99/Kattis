w = int(input())

n = int(input())

areal = 0
for _ in range(n):
    wi, le = [int(x) for x in input().split()]
    areal += wi * le

print(int(areal / w))
