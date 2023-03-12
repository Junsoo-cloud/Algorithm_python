# Num_3(중복순열) - 15651
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

import sys
sys.stdin=open('input.txt', 'r')
def DFS(v):
    if v == m:
        for i in range(m):
            print(a[i], end = ' ')
        print()
        return
    else:
        for i in range(1, n+1):
            a[v] = i
            DFS(v+1)
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [0]*m
    DFS(0)