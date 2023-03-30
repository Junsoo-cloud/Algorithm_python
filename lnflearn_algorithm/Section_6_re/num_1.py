# 10진수 -> 2진수
import sys
sys.stdin=open('input.txt', 'r')
def DFS(n):
    if n == 0:
        return
    else:
        DFS(n//2)
        print(n%2, end = '')
if __name__ == "__main__":
    N = int(input())
    DFS(N)