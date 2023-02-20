'''Num_5: 회의실 배정(그리디 알고리즘)
   그리디 알고리즘의 keyword = 정렬!!
   정렬하는 방식이 문제풀이의 방향성을 결정함'''

import sys
sys.stdin=open('input.txt', 'r')
n = int(input())
meet_times = []
for _ in range(n):
    s, e = map(int, input().split())
    meet_times.append((s, e))
meet_times.sort(key=lambda x: (x[1], x[0]))
et = 0
cnt = 0
for s, e in meet_times:
    if s >= et:
        cnt += 1
        et = e
print(cnt)