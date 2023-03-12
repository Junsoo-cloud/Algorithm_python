'''Num_7: 동전교환(Cut Edge)'''
import sys
sys.stdin=open('input.txt', 'r')
def DFS(l, price):
    global cnt
    if price%t[l] == 0:
        cnt += price//t[l]
        return
    else:
        cnt += price//t[l]
        print(cnt)
        DFS(l+1, price%t[l])
if __name__ == "__main__":
    n = int(input())
    t = list(map(int, input().split()))
    t.sort(reverse=True)
    p = int(input())
    cnt = 0
    DFS(0, p)
    print(cnt)