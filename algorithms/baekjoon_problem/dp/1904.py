#  01 타일
import sys
sys.stdin = open('input.txt', 'r')

# Bottom - up 구현

n = int(input())

dp = [0]*(n+1)

dp[1] = 1
dp[2] = 2

for i in range(1, n//2):
    if i % 2 == 0:
        dp[2*i + 2] = dp[2*i] + 2*i + 1
    dp[2*i + 1] = dp[2*i - 1] + i + 2