import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

arr = list()

for _ in range(n):
    tmp = int(input())
    arr.append(tmp)

arr.sort(reverse = True)
res = list()
for i in range(n):
    tmp = arr[i] * (i+1)
    res.append(tmp)
print(max(res))