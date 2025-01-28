def checkArithmetic(nums, diff):
    for x, y in zip(nums, nums[1:]):
        if abs(x - y) != diff:
            return False

    return True


ant_caser = int(input())

for i in range(ant_caser):
    deler = [int(x) for x in input().split()[1:]]
    diffChecker = abs(deler[0] - deler[1])
    if checkArithmetic(deler, diffChecker):
        print("arithmetic")
    else:
        sortert = sorted(deler)
        if checkArithmetic(sortert, abs(sortert[0] - sortert[1])):
            print("permuted arithmetic")
        else:
            print("non-arithmetic")
