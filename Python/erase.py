n = int(input())

before = input().strip()
after = input().strip()

suksess = True
for i in range(len(before)):
    if (int(before[i]) + n) % 2 != int(after[i]):
        print("Deletion failed")
        suksess = False
        break

if suksess:
    print("Deletion succeeded")
