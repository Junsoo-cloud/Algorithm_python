'''Num_4: 후위 표기식 연산(Stack)'''
import sys
sys.stdin=open('input.txt', 'r')
a = input()
stack = []
tmp = 0
for x in a:
    if x.isdigit():
        stack.append(int(x))
    else:
        if x == '+':
            first = stack.pop()
            second = stack.pop()
            tmp = first + second
            stack.append(tmp)
        elif x == '*':
            first = stack.pop()
            second = stack.pop()
            tmp = first * second
            stack.append(tmp)
        elif x == '-':
            first = stack.pop()
            second = stack.pop()
            tmp = second - first
            stack.append(tmp)
        elif x == '/':
            first = stack.pop()
            second = stack.pop()
            tmp = second / first
            stack.append(tmp)
print(stack[0])