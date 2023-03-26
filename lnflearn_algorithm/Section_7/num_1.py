'''Num_1: 최대점수 구하기 (DFS)'''
import sys
sys.stdin=open('input.txt')
def DFS(L, score, tsum):
    global Max
    if tsum > m:
        return
    if L==n:
        if score > Max:
            Max = score
        return
    else:
        DFS(L+1, score+a[L][0], tsum+a[L][1])
        DFS(L+1, score, tsum)
if __name__ == "__main__":
    a = []
    n, m = map(int, input().split())
    Max = 0
    for _ in range(n):
        s, t = map(int, input().split())
        a.append((s, t))
    DFS(0, 0, 0)
    print(Max)