import sys
sys.stdin=open('input.txt', 'r')
def DFS(L, S):
    if L == m:
        for i in range(m):
            print(res[i], end = ' ')
        print()
        return
    else:
        for i in range(S, n+1):
            res[L] = i
            DFS(L+1, i+1)
if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0]*(n+1)
    cnt = 0
    DFS(0, 1)
    
    
    