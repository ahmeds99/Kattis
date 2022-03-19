import sys 

for i in range(int(sys.stdin.readline())):
    sum = 0
    for tall in sys.stdin.readline().split()[1:]:
        sum += int(tall) - 1
    
    sum += 1
    print(sum)