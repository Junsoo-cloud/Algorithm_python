'''Num_4: 합이 같은 부분집합(DFS: Amazon interview)'''
import sys
sys.stdin=open('input.txt', 'r')
def DFS(v, sums):
    if v == n:
        if sums == (tot-sums):
            print('YES')
            sys.exit(0)
    else:
        DFS(v+1, sums + nums[v])
        DFS(v+1, sums)    # 위에 재귀함수 호출이 끝나면 밑에 재귀함수 호출 !! Stack 에 쌓여가는 것을 생각 !
if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    tot = sum(nums)
    DFS(0, 0)
    