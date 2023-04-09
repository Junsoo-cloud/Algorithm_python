'''Num_6: 알파코드 (DFS)'''
import sys
sys.stdin=open('input.txt', 'r')
def DFS(L, P):
    global cnt
    if L == tmp:
        cnt += 1
        for i in range(P): # P까지 도는것 -> P까지 res에 들어있기때문 !!
            print(chr(res[i]+64), end = '')
        print()
        return
    else:
        for i in range(1, 27):
            if n[L] == i:
                res[P] = i
                DFS(L+1, P+1)
            elif i>=10 and n[L] == i//10 and n[L+1] == i%10:
                res[P] = i
                DFS(L+2, P+1)
if __name__ == "__main__":
    n = list(map(int, input()))
    tmp = len(n)
    res = [0]*tmp
    n.insert(tmp, -1) # indexError 방지
    cnt = 0
    DFS(0, 0)
    print(cnt)
    
# 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
# 프로그래머스 파이썬 정규식