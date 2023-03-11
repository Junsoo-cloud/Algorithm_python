import sys
sys.stdin=open('input.txt', 'r')
def DFS(v):
    if v == m:
        for i in range(m):
            print(a[i], end = ' ')
        print()
        return
    else:
        for i in range(1, n+1):
            a[v] = i
            DFS(v+1)
if __name__ == "__main__":
    n, m = map(int, input().split())
    visited = [False]*(n+1)
    a = [0]*m   
    DFS(0)
