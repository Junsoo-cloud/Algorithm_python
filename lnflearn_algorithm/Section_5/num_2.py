'''Num_2: 쇠막대기(Stack)'''
import sys
sys.stdin=open('input.txt', 'r')
a = input()
stack = []
res = 0
for i in range(len(a)):
    if a[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if a[i-1] == '(':
            res += len(stack)
        else:
            res += 1
print(res)

# https://blog.yena.io/studynote/2018/11/14/Algorithm-Basic.html