'''Num_5: 바둑이 승차(Cut Edge Tech)'''
import sys
sys.stdin=open('input.txt', 'r')
def DFS(v, sums):
    global weight_all
    if v == N:
        weight_all.append(sums)
    else:
        DFS(v+1, sums + weight[v])
        DFS(v+1, sums)
    
if __name__ == "__main__":
    weight = []
    weight_all = []
    weight_res = []
    C, N = map(int, input().split())
    for _ in range(N):
        tmp = int(input())
        weight.append(tmp)
    DFS(0, 0)
    for x in weight_all:
        if x <= C:
            weight_res.append(x)
    print(max(weight_res))
    