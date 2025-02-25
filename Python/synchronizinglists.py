tall = int(input())

while tall != 0:
    first_list = [int(input()) for _ in range(tall)]
    second_list = [int(input()) for _ in range(tall)]

    sorted_first = sorted(first_list)
    sorted_second = sorted(second_list)

    correspondences = {}

    for x, y in zip(sorted_first, sorted_second):
        correspondences[x] = y

    for n in first_list:
        print(correspondences[n])

    tall = int(input())
