'''Num_1: 가장 큰수 (Stack: List)'''
import sys
sys.stdin=open('input.txt', 'r')
num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []
cnt = 0
for x in num:
    while stack and m >0 and x > stack[-1]:
        stack.pop()
        m -= 1
    stack.append(x)
if m != 0:
    stack = stack[:-2]
res = ''.join(map(str, stack))
print(res)