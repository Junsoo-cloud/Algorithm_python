import sys
sys.stdin=open('input.txt', 'r')
n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))
res = 0
p = price[0]    
for x ,y in zip(length, price[1:]):
    if p > y:
        res += x*p
        p = y
    else:
        res += x*p
print(res)