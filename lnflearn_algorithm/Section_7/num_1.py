'''Num_1: 최대점수 구하기(DFS)''' #230405 clear

import sys
sys.stdin=open('input.txt', 'r')
def DFS(L, S, T):
    global Max
    if T > M:
        return
    if L == N:
        if Max < S:
            Max = S
        return
    else:
        DFS(L+1, S+num[L][0], T+num[L][1])
        DFS(L+1, S, T)
if __name__ == "__main__":
    N, M = map(int, input().split())
    num = [list(map(int, input().split())) for _ in range(N)]
    Max = 0
    DFS(0, 0, 0)
    print(Max)