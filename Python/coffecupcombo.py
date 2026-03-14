n = int(input())
lectures = input()

current_coffee = 0
max_lectures_w_coffee = 0

for lec in lectures:
    if lec == "0":
        if current_coffee > 0:
            max_lectures_w_coffee += 1
            current_coffee -= 1
    else:
        current_coffee = 2
        max_lectures_w_coffee += 1

print(max_lectures_w_coffee)
