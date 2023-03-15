'''Num_7 에라토스테네스 체'''
# Brute-Force
n = int(input())
nums = []
for i in range(2, n+1):
    cnt = 0
    for j in range(1, i+1): 
        if i%j == 0:
            cnt += 1
    if cnt == 2:
        nums.append(i)
print(len(nums))


# 소수인 것들의 배수를 다 체에 거르는 느낌



