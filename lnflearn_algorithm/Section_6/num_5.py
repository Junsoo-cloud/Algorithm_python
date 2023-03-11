import sys
sys.stdin=open('input.txt', 'r')
def DFS(v, sums, tsums):
    global res
    if sums > c:
        return
    if sums + (tot-tsums) < res:
        return
    if v == n:
        if sums > res:
            res = sums
    else:
        DFS(v+1, sums + weight[v], weight[v])
        DFS(v+1, sums, weight[v])

if __name__ == "__main__":
    c, n = map(int, input().split())
    weight = []
    res = -2147000000
    for _ in range(n):
        tmp = int(input())
        weight.append(tmp)
    tot = sum(weight)
    DFS(0, 0, 0)
    print(res)