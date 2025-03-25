import statistics

n = int(input())

for _ in range(n):
    info = [int(x) for x in input().split()]
    num_students = info[0]
    grades = info[1:]

    avg = statistics.fmean(grades)
    num_over_avg = len(list(filter(lambda x: x > avg, grades)))
    percent = num_over_avg / num_students * 100

    print(f"{percent:.3f}%")
