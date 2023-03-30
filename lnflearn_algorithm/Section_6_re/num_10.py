import sys
sys.stdin=open('input.txt', 'r')
def DFS(L, S):
    if L == M:
        print(' '.join(map(str, res)))
        return
    else:
        for i in range(S, N+1):
            if i not in res:
                res.append(i)
                DFS(L+1, i+1)
                res.pop()
if __name__ == "__main__":
    N, M = map(int, input().split())
    res = []
    DFS(0, 1)