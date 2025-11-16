bowls, consecutive = [int(x) for x in input().split()]

nums = [int(x) for x in input().split()]

biggest = 0
for n in range(len(nums) - consecutive + 1):
    sum = 0
    for i in range(consecutive):
        sum += nums[n + i]

    if sum > biggest:
        biggest = sum

print(biggest)
