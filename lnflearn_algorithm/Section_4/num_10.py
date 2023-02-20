'''Num_10: 역수열(그리디 알고리즘)'''
import sys
sys.stdin=open('input.txt', 'r')
n = int(input())
nums = list(map(int, input().split()))
origin_nums = [0]*n
cnt = 0
for i in range(n):
    for j in range(n):
        if nums[i] ==0 and origin_nums[j] == 0: # num[i] -> 1,2,3, 숫자들이 0개이고 & 역수열의 값도 0일때
            origin_nums[j] = i+1
            break
        elif origin_nums[j] == 0:
            nums[i] -= 1
for x in origin_nums:
    print(x, end = ' ')