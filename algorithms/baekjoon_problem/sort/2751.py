# 수 정렬하기 2

import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)
nums.sort()
for num in nums:
    print(num)