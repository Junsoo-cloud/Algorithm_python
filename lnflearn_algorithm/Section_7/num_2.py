'''Num_2: 휴가 (DFS)''' # 230405 clear
import sys
sys.stdin=open('input.txt', 'r')
def DFS(L, B):
    global Max
    if L >= N:
        if B > Max:
            Max = B
        return
    else:
        DFS(L+num[L][0] , B+num[L][1])
        DFS(L+1, B)
if __name__ == "__main__":
    N = int(input())
    num = []
    for _ in range(N):
        T, P = map(int, input().split())
        num.append((T, P))
    Max = 0
    DFS(0, 0)
    print(Max) # 60