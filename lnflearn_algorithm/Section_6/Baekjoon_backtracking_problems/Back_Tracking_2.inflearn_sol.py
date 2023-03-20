import sys
sys.stdin=open('input.txt', 'r')
def DFS(L, V):
    if len(res) == m:
        print(' '.join(map(str, res)))
    else:
        for i in range(V, n+1): # 전에 골랬던 숫자+1 부터 상태 트리로 뻗는 for문 !!
            res.append(i)
            DFS(L+1, i+1)
            res.pop()
if __name__ == "__main__":
    n, m = map(int, input().split())
    res = []
    DFS(1, 1)