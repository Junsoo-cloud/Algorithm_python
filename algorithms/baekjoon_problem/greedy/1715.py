import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = list()
for _ in range(n):
    tmp = int(input())
    arr.append(tmp)
arr.sort()
arr.insert(0, 0)
past_res = list()
res = list()
tmp = 0
for i in range(1, n+1):
    tmp += arr[i]
    if i%2 == 0:
        past_res.append(tmp)
        res.append(tmp)
        tmp = 0
if tmp:
    res.append(tmp)
if n%2 == 0:
    print(sum(res)*2)
else:
    print(sum(past_res) + sum(res))