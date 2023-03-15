'''Num_9: 순열 구하기 (DFS)'''
import sys
sys.stdin=open('input.txt', 'r')
def DFS(v):
    global cnt
    if v == m:
        cnt += 1
        for i in range(m):
            print(a[i], end = ' ')
        print()
    else:
        for i in range(1, n+1):
            if i not in a:
                a.append(i)
                DFS(v+1)
                a.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    cnt = 0
    DFS(0)
    print(cnt)