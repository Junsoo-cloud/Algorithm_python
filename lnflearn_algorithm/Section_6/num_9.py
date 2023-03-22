'''Num_9: 수열 추측하기'''
import sys
sys.stdin=open('input.txt', 'r')
def DFS(L, tot):
    if L == n and tot == f:
        print(' '.join(map(str, p)))
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L+1, tot+p[L]*s[L])
                ch[i] = 0    
if __name__ == "__main__":
    n, f = map(int, input().split())
    s = [1]*(n)
    p = [0]*n
    ch = [0]*(n+1)
    for i in range(1, n):
        s[i] = s[i-1]*(n-i)/i
    DFS(0, 0)
    