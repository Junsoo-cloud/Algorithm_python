'''Num_3: 후위표기식 만들기(Stack)'''
import sys
sys.stdin=open('input.txt', 'r')
a = input()
stack = [] # 연산 기호들을 담는 stack
res = ''
for x in a:
    if x.isdigit(): # x가 숫자인지 판별
        res += x
    else:
        if x == '(': # x가 여는 괄호 일 때
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'): # */ 랑 같으면 */ 하나 pop -> res에 출력
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1]!= '(': # 여는 괄호 전까지 출력
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1]!= '(': # 여는 괄호 만날때까지 출력(pop)
                res += stack.pop()
            stack.pop() # 여는 괄호 삭제
while stack: # 남은 기호 있을 때
    res += stack.pop() # 기호를 모두 출력
print(res)