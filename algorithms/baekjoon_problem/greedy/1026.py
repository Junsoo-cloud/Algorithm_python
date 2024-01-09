import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))


arr_A.sort()
arr_B.sort(reverse = True)

ssum = 0

for i in range(n):
    ssum += arr_A[i] * arr_B[i]
print(ssum)