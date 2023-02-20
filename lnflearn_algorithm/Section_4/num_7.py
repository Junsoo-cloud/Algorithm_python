'''Num_7: 창고정리(그리디 알고리즘)'''
import sys
sys.stdin=open('input.txt', 'r')
l = int(input())
room = list(map(int, input().split()))
m = int(input())
room.sort()
for _ in range(m):
    room[0] += 1
    room[l-1] -= 1
    room.sort()
print(room[l-1] - room[0])