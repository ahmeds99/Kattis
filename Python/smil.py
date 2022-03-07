import sys

data = list(sys.stdin.readline())
smilAdresse = []

for i in range(len(data)):
    if (data[i] == ":" or data[i] == ";") and i + 1 < len(data):
        if data[i + 1] == ")":
            smilAdresse.append(i)
        elif data[i + 1] == "-" and i + 2 < len(data):
            if data[i + 2] == ")":
                smilAdresse.append(i)
        i += 1

for smil in smilAdresse:
    print(smil)