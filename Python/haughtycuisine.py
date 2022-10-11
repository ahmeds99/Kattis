import sys

retter = []

num_dishes = int(sys.stdin.readline())
for _ in range(num_dishes):
    info = sys.stdin.readline().strip().split()
    retter.append((info[0], info[1:]))

print(retter[0][0])
for dish in retter[0][1]:
    print(dish)