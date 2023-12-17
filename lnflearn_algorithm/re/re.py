import sys
sys.stdin=open('input.txt', 'r')
N = int(input())
details = []
for _ in range(N):
    height, weight = map(int, input().split())
    details.append((height, weight))
details.sort(reverse=True)
cnt = 0
# for i in range(N):
#     for j in range(i, N):
#         if details[i][1] < details[j][1]:
#             cnt += 1
Max = 0
for x, y in details:
    if y > Max:
        Max = y
        cnt += 1
print(cnt)