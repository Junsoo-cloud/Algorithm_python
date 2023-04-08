import sys
sys.stdin=open('input.txt', 'r')
def DFS(L, A, B, C):
    global Min
    if L == N:
        tmp = {A, B, C}
        x = max(tmp) - min(tmp)
        if Min > x:
            if len(tmp) == 3:
                Min = x 
        return
    else:
        DFS(L+1, A+num[L], B, C)
        DFS(L+1, A, B+num[L], C)
        DFS(L+1, A, B, C+num[L])
if __name__ == "__main__":
    N = int(input())
    num = []
    res = [0]*3
    for _ in range(N):
        tmp = int(input())
        num.append(tmp)
    Min = 2147000000
    DFS(0, 0, 0, 0)
    print(Min)
    
    