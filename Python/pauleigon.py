import sys

N, P, Q = [int(x) for x in sys.stdin.readline().split(" ")]

points_at_time = P + Q
num_rounds = int(points_at_time / N)
print("paul") if num_rounds % 2 == 0 or points_at_time < N else print("opponent")
