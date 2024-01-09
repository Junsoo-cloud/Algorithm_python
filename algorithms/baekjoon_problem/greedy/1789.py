import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

ssum = 0
for i in range(1, n+1):
    ssum += i
    if ssum > n:
        print(i-1)
        break
    if ssum == n:
        print(i)
        break