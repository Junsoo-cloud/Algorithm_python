'''Num_6'''
def digit_sum(x: int) -> int:
    sums = 0
    for s in str(x):
        sums += int(s)
    return sums

# while x>0:
#     sum += x%10
#     x = x//10
n = int(input())
nums = list(map(int, input().split()))
Max = -2147000000
for i in range(n):
    x = digit_sum(nums[i])
    if Max < x:
        Max = x
        idx = i
print(nums[idx])

# 지역변수, 전역변수에 대한 개념 공부 필요할 듯

