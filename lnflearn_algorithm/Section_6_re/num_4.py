import sys
sys.stdin=open('input.txt', 'r')
def DFS(L, tot):
    if L == N:
        if tot == (s-tot):
            print('YES')
            sys.exit(0) # sys.exit(0) -> 종료
        return
    else:
        DFS(L+1, tot+nums[L])
        DFS(L+1, tot)
if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    s = sum(nums)
    DFS(0, 0)