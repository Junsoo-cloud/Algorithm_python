'''Num_5'''
# 내 풀이는 for문을 줄인다고 해서 이렇게 했는데, 뭔가 정돈이 하나도 안된 느낌 ..
from collections import defaultdict
n, m = map(int, input().split())
sums = []
sums_dict = defaultdict(int)
for i in range(n):
    for j in range(m):
        sums.append((i+1)+(j+1))
for x in sums:
    sums_dict[x] += 1
a = max(sums_dict.values())
print([k for k, v in sums_dict.items() if v == a ])


# 이중 for문 그리고 for문
n, m = map(int, input().split())
cnt = [0] * (n+m+3)
Max = -2147000000
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1
for i in range(2, n+m+1):
    if cnt[i] > Max:
        Max = cnt[i]
for i in range(2, n+m+1):
    if cnt[i] == Max:
        print(i, end=' ')
        