'''Num_3: 양팔저울 (DFS)''' 
import sys
sys.stdin=open('input.txt', 'r')
def DFS(v):
    if v == k:
        a = []
        for i in range(k):
            if ch[i] == 1:
                a.append(num[i])
        a_set.append(a)
        return
    else:
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)
if __name__ == "__main__":
    k = int(input())
    num = list(map(int, input().split()))
    original = list(range(1, sum(num)+1))
    original = set(original)
    ch = [0]*k
    a_set = []
    res = set()
    DFS(0)
    for i in range(len(a_set)-2):
        for j in range(i+1, len(a_set)):
            tmp = sum(a_set[i])-sum(a_set[j])
            res.add(abs(tmp))
    print(len(original) - len(res))