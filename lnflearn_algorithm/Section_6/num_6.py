'''Num_6: 중복순열 구하기(DFS)'''
import sys
sys.stdin=open('input.txt', 'r')
def DFS(v):
    global cnt
    if v == n-1:
        cnt += 1
        for i in range(m):
            print(a[i], end = ' ')
        print()
        return
    else:
        for i in range(1, n+1): # 상태 트리의 수
            a[v] = i
            DFS(v+1)
if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    a = [0]*m
    DFS(0)
    print(cnt)