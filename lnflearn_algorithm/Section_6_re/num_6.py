import sys
sys.stdin=open('input.txt', 'r')
def DFS(L):
    if L == M:
        print(' '.join(map(str, res)))
        return
    else:
        for i in range(1, N+1):
            res.append(i)
            DFS(L+1)
            res.pop()
if __name__ == "__main__":
    N, M = map(int, input().split())
    res = []
    DFS(0)