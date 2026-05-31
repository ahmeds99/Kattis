n = int(input())

tot = 0
for _ in range(n):
    num = input()
    if 12 <= len(num) <= 13 and num.startswith("+39"):
        tot += 1

print(tot)
