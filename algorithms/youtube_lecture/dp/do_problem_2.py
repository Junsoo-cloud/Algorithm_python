import sys
sys.stdin = open('input.txt', 'r')
# 정수 n 입력받기
n = int(input())
# 앞서 계산된 결과 저장하기 위해 DP table 초기화 -> 최적의 해 (Optimal Solution Dp table)
d = [0]*30001

for i in range(2, n+1):  # bottom-up
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    elif i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
    elif i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
print(d[n])
    