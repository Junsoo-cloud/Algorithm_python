'''Num_6: 알파코드(DFS)'''
import sys
sys.stdin=open('input.txt', 'r')
def DFS(L, P):
    global N
    print(N)
    if L == len(N):
        print(res)
        return
    else:
        for i in range(1, 27):
            if N[L] == str(i):
                if len(str(i)) == 1:
                    res[P] == i
                    DFS(L+1, P+1)
                if len(str(i)) == 2 and i <= 26:
                    res[P] == i
                    DFS(L+2, P+1)
if __name__ == "__main__":
    N = str(input())
    res = [0]*(len(N)+3)
    DFS(0, 0)