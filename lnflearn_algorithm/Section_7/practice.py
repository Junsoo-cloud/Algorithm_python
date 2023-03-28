# 5 0
# -7 -3 -2 5 8
import sys
sys.stdin=open('input.txt', 'r')
def DFS(L, F):
    print(sum(res))
    global cnt
    if L == N:
        if sum(res) == S:
            cnt += 1
        return
    else:
        for i in range(F, N):
            res[L] = nums[i]
            DFS(L+1, i+1)
if __name__ == "__main__":
    N, S = map(int, input().split())
    nums = list(map(int, input().split()))
    res = [0]*N
    cnt = 0 
    DFS(0, 0)
    print(cnt)