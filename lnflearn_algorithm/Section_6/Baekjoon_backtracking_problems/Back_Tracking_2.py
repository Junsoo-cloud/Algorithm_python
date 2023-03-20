# Num_2 - 15650
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다. !!!!

import sys
sys.stdin=open('input.txt', 'r')
def DFS(v):
    if len(res) == m:
        print(' '.join(map(str, res)))
    for i in range(v, n+1): # 결국은 v가 증가하면서 증가수열 생성
        if i not in res:
            res.append(i)
            DFS(i)
            res.pop()
if __name__ == "__main__":
    n, m = map(int, input().split())
    res = []
    DFS(1)