import sys

correct = sys.stdin.readline().split()
wrong = sys.stdin.readline().split()

alleFeil = {}

for i in range(len(correct)):
    if len(correct[i]) != len(wrong[i]):
        print(correct[i])
        for j in range(len(correct[i])):
            if correct[i][j] != wrong[i][j]:
                alleFeil[wrong[i][j]] = wrong[i][j]

print(alleFeil)
