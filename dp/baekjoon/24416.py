import sys
sys.stdin=open('input.txt', 'r')
N = int(input())
cnt_recursion = 0
cnt_dp = 0
d = [0]*10000
# recursion (완전탐색) function 설정
def fibo_recursion(n): 
    global cnt_recursion
    # 종료 조건
    if n == 1 or n == 2:
        return 1
    cnt_recursion += 1
    return fibo_recursion(n-1) + fibo_recursion(n-2)
# dp function 설정
def fibo_dp(n):
    global cnt_dp
    # 종료 조건
    if n == 1 or n == 2:
        return 1
    # memoization
    if d[n] != 0:
        return d[n]
    cnt_dp += 1
    d[n] = fibo_dp(n-1) + fibo_dp(n-2)
    return d[n]

x = fibo_recursion(N)
y = fibo_dp(N)
print(cnt_recursion+1, cnt_dp)



