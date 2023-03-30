import sys
sys.stdin=open('input.txt', 'r')
def DFS(L, S):
    if L == N:
        return
    else:
        for i in range(S, N):
            res.append(num[i])
            DFS(i+1)
            res.pop()
if __name__ == "__main__":
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    num.sort()
    res = []
    DFS(0)