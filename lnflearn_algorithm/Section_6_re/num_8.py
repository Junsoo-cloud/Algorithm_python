import sys
sys.stdin=open('input.txt', 'r')
def DFS(L):
    global cnt
    if L == M:
        cnt += 1
        print(' '.join(map(str, res)))
        return
    else:
        for i in range(1, N+1):
            if i not in res:
                res.append(i)
                DFS(L+1)
                res.pop()
if __name__ == "__main__":
    N, M = map(int, input().split())
    res = []
    cnt = 0
    DFS(0)
    print(cnt)