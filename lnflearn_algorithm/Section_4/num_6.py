'''Num_6: 씨름 선수(그리디 알고리즘)'''
import sys
sys.stdin=open('input.txt', 'r')
n = int(input())
members = []
for _ in range(n):
    height, weight = map(int, input().split())
    members.append((height, weight))
members.sort()
cnt = 0
for height_s, weight_s in members:
    for height, weight in members:
            if height_s > height and weight_s > weight:
                cnt += 1
print(n-cnt)