'''Num_5: 동전 분배하기(DFS)'''
import sys
sys.stdin=open('input.txt', 'r')
def DFS(L):
    global Min
    if L == N:
        a = max(res) - min(res)
        if Min > a:
            x = set()
            for i in range(3):
                x.add(res[i])
                if len(x) == 3:
                    Min = a
    else:
        for i in range(3):
            res[i] += num[L]
            DFS(L+1)
            res[i] -= num[L]
if __name__ == "__main__":
    N = int(input())
    num = []
    res = [0]*3
    for _ in range(N):
        tmp = int(input())
        num.append(tmp)
    Min = 2147000000
    DFS(0)
    print(Min)