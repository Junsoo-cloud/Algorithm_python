import sys
sys.stdin=open('input.txt', 'r')
def DFS(x, y):
    if x<= -1 or x>= M or y<= -1 or y>= N:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        DFS(x, y-1)
        DFS(x+1, y)
        DFS(x, y+1)
        DFS(x-1, y)
        return True
    return False
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
        result = 0
    for i in range(M):
        for j in range(N):
            if DFS(i, j) == True:
                result += 1
    print(result)