import sys

oversikt = [["A"], ["B"], ["C"], ["D"], ["E"],]

limits = [int(x) for x in sys.stdin.readline().split()]
grade = int(sys.stdin.readline())

for i in range(len(limits)):
    oversikt[i].append(limits[i])

for element in oversikt:
    if grade >= element[1]:
        print(element[0])
        exit(0)

print("F")
