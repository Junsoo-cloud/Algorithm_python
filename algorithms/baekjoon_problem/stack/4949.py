import sys
sys.stdin = open('input.txt', 'r')
while (1):
    temp = input()
    stack = list()
    if temp == ".":
        break
    for x in temp:
        if x == "(" or x == "[":
            stack.append(x)
        elif x == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(')')
                break
        elif x == "]":
            if len(stack) != 0 and stack[-1] == "[": 
                    stack.pop()
            else:
                stack.append(']')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')