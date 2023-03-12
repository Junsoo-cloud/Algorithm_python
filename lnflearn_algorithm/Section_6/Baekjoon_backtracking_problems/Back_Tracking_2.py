# Num_2 - 15650
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다. !!!!

import sys
sys.stdin=open('input.txt', 'r')
def DFS(v):
    if v == m:
        for i in range(m):
            print(a[i], end = ' ')
        print()
        return
    else:
        for i in range(v+1, n+1):
            if i not in a:
                a.append(i)
                DFS(v+1)
                a.pop()
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    DFS(0)