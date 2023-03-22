'''Num_10: 조합 구하기'''
import sys
sys.stdin=open('input.txt', 'r')
def DFS(v):
    global cnt
    if len(s) == m:
        cnt += 1
        print(' '.join(map(str, s)))
        return
    else:
        for i in range(v, n+1):
            if i not in s:
                s.append(i)
                DFS(i)
                s.pop()
if __name__ == "__main__":
    n, m =map(int, input().split())
    s = []
    cnt = 0
    DFS(1)
    print(cnt)