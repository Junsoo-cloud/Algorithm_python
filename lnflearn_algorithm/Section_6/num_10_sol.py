'''Num_10: 조합 구하기 
DFS parameter 두개로 설정하기 '''
import sys
sys.stdin=open('input.txt', 'r')
def DFS(L, S):
    global cnt
    if L == m:
        cnt += 1
        for j in range(L):
            print(res[j], end = ' ')
        print()
    else:
        for i in range(S, n+1): # 전 Node + 1 부터 for문을 돌도록
            res[L] = i
            DFS(L+1, i+1)
if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0]*(n+1)
    cnt = 0
    DFS(0, 1)