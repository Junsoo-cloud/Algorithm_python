import sys
sys.stdin=open('input.txt', 'r')
# 정수 N 입력 받기
N = int(input())
# 모든 식량 정보 입력 받기
array = list(map(int, input().split()))

# 앞서 계산된 결과 저장하기 위해 DP table 초기화 -> 최적의 해 (Optimal Solution Dp table)
d = [0]*100

# DP -> bottom-up
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2]+array[i])
print(d[N-1])