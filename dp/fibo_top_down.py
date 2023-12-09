# Memoization 하기 위해 리스트 초기화
d = [0]*100

# top-down recursion function 구현 -> 구해야 하는 값을 부르고 나서 밑으로 가면서 값을 쪼개서 구하는 방법

def fibo(n):
    # 종료 조건
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fibo(n-1) + fibo(n-2)
    return d[n]
print(fibo(99))