import sys

codeLines, formatErrors = [int(n) for n in sys.stdin.readline().split()]
errors = [int(n) for n in sys.stdin.readline().split()]
errorsSet = set(errors)

errorValues = []
previous = errors[0]
currentString = str(previous)
for n in errors[1:]:
    if n != previous + 1:
        if currentString != str(previous):
            currentString += "-" + str(previous)
        errorValues.append(currentString)
        currentString = str(n)

    previous = n

if currentString != str(previous):
    currentString += "-" + str(previous)
errorValues.append(currentString)

correctValues = []
firstValid = 0
for i in range(1, codeLines):
    if i not in errorsSet:
        firstValid = i
        break

previous = firstValid
currentString = str(previous)
for i in range(firstValid + 1, codeLines + 1):
    if i in errorsSet:
        if int(currentString) not in errorsSet:
            if currentString != str(previous):
                currentString += "-" + str(previous)
            correctValues.append(currentString)
        currentString = str(i + 1)

    previous = i

if int(currentString) < codeLines:
    if int(currentString) not in errorsSet and currentString != str(previous):
        currentString += "-" + str(previous)
    correctValues.append(currentString)

print("Errors: ", end="")
if len(errorValues) > 1:
    print(*errorValues[:-1], sep=", ", end="")
    print(f" and {errorValues[-1]}")
else:
    print(*errorValues, sep=", ")

print("Correct: ", end="")
if len(correctValues) > 1:
    print(*correctValues[:-1], sep=", ", end="")
    print(f" and {correctValues[-1]}")
else:
    print(*correctValues, sep=", ")
