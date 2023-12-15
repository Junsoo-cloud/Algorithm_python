# 앞서 계산한 결과를 저장하기 위한 DP table 초기화
d = [0]*100

# 1,2 번째 피보나치 수 초기화
d[1] = 1
d[2] = 1
n = 99

# 반복문으로 bottom-up 구현 -> 작은 문제들을 먼저 구하고 계속 더해나가는 과정
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])

# 20분부터 강의 들으면 됨    https://www.youtube.com/watch?v=5Lu34WIx2Us 

