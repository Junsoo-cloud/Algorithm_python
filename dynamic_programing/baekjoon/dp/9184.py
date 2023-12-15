import sys
sys.stdin=open('input.txt', 'r')

# 3차원 리스트
def w(a,b,c):
    if a_memo[a] != 0 and b_memo[b] != 0 and c_memo[c] != 0:
        return (a_memo[a], b_memo[b], c_memo[c])
    else:
        a_memo[a], b_memo[b], c_memo[c] = dp()
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return dp(20, 20, 20)
    elif a < b and b < c:
        return dp(a, b, c-1) + dp(a, b-1, c-1) - dp(a, b-1, c)
    else:
        return dp(a-1, b, c) + dp(a-1, b-1, c) + dp(a-1, b, c-1) - dp(a-1, b-1, c-1)
dp = [[[0]*(21) for _ in range(21)]]
while True:
    nums = list(map(int, input().split()))
    if nums[0] == nums[1] == nums[2] == -1:
        break

