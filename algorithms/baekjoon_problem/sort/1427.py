import sys
sys.stdin = open('input.txt', 'r')
n = input()
nums= []
for x in n:
    nums.append(int(x))
nums.sort(reverse = True)
for x in nums:
    print(x, end = '')