import sys
sys.stdin = open('input.txt', 'r')
nums = []
for _ in range(5):
    num = int(input())
    nums.append(num)
print(sum(nums)//5)

nums.sort()
print(nums[5//2])