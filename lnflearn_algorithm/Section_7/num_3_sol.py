'''Num_3: 양팔저울 (DFS)''' 
import sys
sys.stdin=open('input.txt', 'r')
def DFS(L, tot):
    if L == n:
        if 0< tot <= s: # +- 대칭 
            res.add(abs(tot))
        return
    else:
        DFS(L+1, tot+G[L])
        DFS(L+1, tot-G[L])
        DFS(L+1, tot)
if __name__ == "__main__":
    n = int(input())
    G = list(map(int, input().split()))
    s = sum(G)
    res = set()
    DFS(0, 0)
    print(s-len(res))