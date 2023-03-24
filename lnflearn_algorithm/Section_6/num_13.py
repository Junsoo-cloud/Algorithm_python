'''Num_13: 경로 탐색(DFS)'''
import sys
sys.stdin=open('input.txt', 'r')
def DFS(v):
    global cnt
    if v == n:
        cnt += 1
        return
    else:
        for i in range(1, n+1):
            if ch[i] == 0 and matrix[v-1][i-1] == 1:
                res.append(i)
                ch[i] = 1
                DFS(i)
                ch[i] = 0
                res.pop()
if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = [[0]*n for _ in range(n)]
    for _ in range(m):
        n1, n2 = map(int, input().split())
        matrix[n1-1][n2-1] = 1
    ch = [0]*(n+1)
    ch[1] = 1
    res = [1]
    cnt = 0
    DFS(1)
    print(cnt)