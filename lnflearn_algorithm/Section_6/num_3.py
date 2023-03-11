'''Num: 부분집합 구하기(DFS, 상태트리)'''
import sys
sys.stdin=open('input.txt', 'r')
def DFS(v):
    if v == n+1: # Base_case: 모든 노드를 순회했을때 지금까지 쌓여있는 부분집합 출력
        for i in range(1, n+1):
            if ch[i] == 1: # v번째 Node가 부분집합에 속할 때
                print(i, end = ' ') # i (Node) 출력
    else: # 상태트리 순회
        
        ch[v] = 1 # v번째 Node가 부분집합에 속할 때
        DFS(v+1) # 다음 Node 순회
        ch[v] = 0 # v번째 Node가 부분집합에 속하지 않을 때
        DFS(v+1) # 다음 Node 순회
if __name__ == "__main__":
    n = int(input())
    ch = [0]*(n+1)
    DFS(1)