'''Num_7: 동전 교환 (Cut Edge !!)'''
import sys
sys.stdin=open('input.txt', 'r')
def DFS(L, tot):
    global res
    if tot == p:
        res = L
        return
    if tot > p:
        return
    if L > res:
        return
    else:
        for i in range(n):
            DFS(L+1, tot+a[i])
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    p = int(input())
    a.sort(reverse=True)
    res = 2147000000
    DFS(0, 0)
    print(res)