# 연속합
import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

arr = list(map(int, input().split()))
d = [-1001]*(n)

for i in range(n):
    for j in range(i+1):
        if d[i] <= sum(arr[j:i+1]):
            d[i] = sum(arr[j:i+1])
print(max(d))