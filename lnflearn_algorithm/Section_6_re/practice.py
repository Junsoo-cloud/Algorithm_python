import sys
sys.stdin=open('input.txt', 'r')
def DFS(S):
    if len(res) == M:
        f_res.add(tuple(res))
        return
    else:
        for i in range(S, N):
            res.append(num[i])
            DFS(i)
            res.pop()
if __name__ == "__main__":
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    num.sort()
    res = []
    f_res = set()
    DFS(0)
    f_res = sorted(list(f_res))
    for x in f_res:
        print(*x)