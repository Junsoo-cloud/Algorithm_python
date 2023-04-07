'''Num_4: 동전 바꿔주기'''
import sys
sys.stdin=open('input.txt', 'r')
def DFS(L, S):
    global cnt
    if S > T:
        return
    if L == k:
        if S == T:
            cnt += 1
        return
    else:
        for i in range(num[L][1]+1): # for 문에서 0 부터 시작하기 때문에, DFS(L+1, S) <- 구현 X 
            DFS(L+1, S+num[L][0]*i)
if __name__ == "__main__":
    T = int(input())
    k = int(input())
    num = []
    cnt = 0
    for _ in range(k):
        p, n = map(int, input().split())
        num.append((p,n))
    DFS(0, 0)
    print(cnt)