import sys
from collections import deque
sys.stdin=open('input.txt', 'r')
def DFS(S):
    ch_1[S] = 1
    print(S, end = ' ')
    for j in range(1, N+1):
        if graph[S][j] == 1 and ch_1[j] == 0:
            DFS(j)
            ch_1[j] = 1
def BFS(S):
    Q = deque([S])
    ch_2[S] = 1
    while Q:
        tmp = Q.popleft()
        print(tmp, end = ' ')
        for i in range(N+1):
            if graph[tmp][i] == 1 and ch_2[i] == 0:
                Q.append(i)
                ch_2[i] = 1
if __name__ == "__main__":
    N, M, S = map(int, input().split())
    graph = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1
        
    ch_1 = [0]*(N+1)
    ch_2 = [0]*(N+1)
    DFS(S)
    print()
    BFS(S)
