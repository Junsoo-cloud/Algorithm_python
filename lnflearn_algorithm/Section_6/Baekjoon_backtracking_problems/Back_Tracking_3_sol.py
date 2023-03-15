import sys
sys.stdin=open('input.txt', 'r')
def DFS(v):
    if len(res) == m: # Index로 접근 X
        print(' '.join(map(str, res)))
        return
    for i in range(v, n+1):  # 첫 시작을 v부터 
        if i not in res:
            res.append(i)
            DFS(i+1)
            res.pop()
if __name__ == "__main__":
    n, m = map(int, input().split())
    res = []
    DFS(1)