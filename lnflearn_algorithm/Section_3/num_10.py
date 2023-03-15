'''num_10: 스도쿠 검사'''
import sys
sys.stdin=open('input.txt', 'r')
a = [list(map(int, input().split())) for _ in range(9)]
for i in range(9):
    ch1 = [0]*10
    ch2 = [0]*10
    sums = 0
    for j in range(9):
        ch1[a[i][j]] = 1
        ch2[a[j][i]] = 1
    if sum(ch1) != 9 or sum(ch2) != 9:
        return False
    for i in range(3):
        for j in range(3):
        ch3 = [0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*]]
# for문을 잘 활용 & index 접근
        