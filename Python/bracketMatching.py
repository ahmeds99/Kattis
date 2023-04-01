import sys

antLinjer = sys.stdin.readline()
stack = []

linje = sys.stdin.readline().strip()

status = True
for char in linje:
    if char == "(":
        stack.append(char)
    elif char == "{":
        stack.append(char)
    elif char == "[":
        stack.append(char)

    else:
        if not stack:
            status = False
            break
        lastChar = stack[-1]
        if char == ")" and lastChar != "(":
            status = False
            break
        elif char == "}" and lastChar != "{":
            status = False
            break
        elif char == "]" and lastChar != "[":
            status = False
            break

        stack.pop()

if stack:
    status = False
print("Valid" if status else "Invalid")
