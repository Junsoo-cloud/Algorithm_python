import sys
sys.stdin=open('input.txt', 'r')
N, M, K = map(int, input().split())
while True:
    if K == 0:
        
    if N//2 > M:
        N -= 2
    else:
        M -= 1
    K -= 1