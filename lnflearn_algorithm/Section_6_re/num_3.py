import sys
sys.stdin=open('input.txt', 'r')
def DFS(L):
    if L == N+1:
        for i in range(1, N+1):
            if ch[i] == 1:
                print(i, end = ' ')
        print()
    else: # check 변수
        ch[L] = 1
        DFS(L+1)
        ch[L] = 0
        DFS(L+1)
if __name__ == "__main__":
    N = int(input())
    ch = [0]*(N+1)
    DFS(1)