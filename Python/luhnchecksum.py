import sys

numCases = int(sys.stdin.readline().strip())

for i in range(numCases):
    number = list(sys.stdin.readline().strip()[::-1])

    for j in range(1, len(number), 2):
        double = int(number[j]) * 2
        if (double) > 9:
            newNumStr = str(double)
            newNum = int(newNumStr[0]) + int(newNumStr[1])
            number[j] = str(newNum)
        else:
            number[j] = str(double)

    sum = 0
    for num in number:
        sum += int(num)
    print("PASS" if sum % 10 == 0 else "FAIL")
