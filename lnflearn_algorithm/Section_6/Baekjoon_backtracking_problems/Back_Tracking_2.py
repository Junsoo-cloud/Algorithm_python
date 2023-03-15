# Num_2 - 15650
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다. !!!!

import sys
sys.stdin=open('input.txt', 'r')
# Sol_1: N으로 설정 -> 종료조건을 M으로 설정
def DFS(n, lst):
    if n > N:
        if len(lst) == M:
            ans.append(lst)
        return
    DFS(n+1, lst+[n]) 
    DFS(n+1, lst)
if __name__ == "__main__":
    ans = []
    N, M = map(int, input().split())
    DFS(1, [])
    for a in ans:
        print(*a)