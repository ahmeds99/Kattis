import sys

totalScore = 0
antallSpm = int(sys.stdin.readline())

forrigeSvar = None
for i in range(antallSpm):
    svar = sys.stdin.readline()
    if forrigeSvar != None and forrigeSvar == svar:
        totalScore += 1
    else:
        forrigeSvar = svar

print(totalScore)
