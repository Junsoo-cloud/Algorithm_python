import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
nums = sorted(list(map(int, input().split())))
m = int(input())
target_nums = list(map(int, input().split()))

for target in target_nums: 
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            print(1, end = ' ')
            break
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    if nums[mid] != target:
        print(0, end = ' ')