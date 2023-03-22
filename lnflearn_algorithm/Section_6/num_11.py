'''Num_11: 수들의 조합'''
import sys
sys.stdin=open('input.txt', 'r')
def DFS(L, V):
    global cnt
    if L == k:
        if sum(res)%m == 0:
            cnt += 1
        return
    else:
        for x in s:
            if V < x:
                res.append(x)
                print(res)
                DFS(L+1, x)
                res.pop()
if __name__ == "__main__":
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    m = int(input())
    res = []
    cnt = 0
    DFS(0, 0)
    print(cnt)
