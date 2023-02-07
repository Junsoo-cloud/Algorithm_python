def digit_sum(x: int) -> int:
    sums = 0
    for s in str(x):
        sums += int(s)
    return sums

n = int(input())
nums = list(map(int, input().split()))
Max = -2147000000
for i in range(n):
    x = digit_sum(nums[i])
    if Max < x:
        Max = x
        idx = i
print(nums[idx])
    