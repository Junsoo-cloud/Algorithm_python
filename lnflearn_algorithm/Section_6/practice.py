import sys
sys.stdin=open('input.txt', 'r')
def checking(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False
    return True
def DFS(v):
    global cnt
    if v == N:
        cnt += 1
        return
    else:
        for i in range(N):
            row[v] = i
            if checking(v):
                DFS(v+1)
if __name__ == "__main__":
    N = int(input())
    row = [0]*N
    cnt = 0
    DFS(0)
    print(cnt)
