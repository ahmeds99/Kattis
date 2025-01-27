from sys import stdin

variables = {}


def evalLine(left, operand, right):
    if left not in variables or right not in variables:
        return "undefined"
    else:
        match operand:
            case "=":
                return variables[left] == variables[right]
            case "<":
                return variables[left] < variables[right]
            case ">":
                return variables[left] > variables[right]


for inp in stdin:
    deler = inp.split()
    if deler[0] == "define":
        variables[deler[2]] = int(deler[1])
    else:
        print(str(evalLine(deler[1], deler[2], deler[3])).lower())
