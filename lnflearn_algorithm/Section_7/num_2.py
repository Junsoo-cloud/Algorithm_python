'''Num_2: 휴가(DFS 활용)'''
import sys
sys.stdin=open('input.txt', 'r')
def DFS(L, time, tot_sum):
    global Max
    if time > N:
        return
    if L >= N:
        if tot_sum > Max:
            Max = tot_sum
        return
    else:
        DFS(L+num[L][0], time+num[L][0], tot_sum+num[L][1])
        DFS(L+1, time, tot_sum)
if __name__ == "__main__":
    N = int(input())
    num = []
    Max = 0
    for _ in range(N):
        t, p = map(int, input().split())
        num.append((t, p))
    DFS(0, 0, 0)
    print(Max)