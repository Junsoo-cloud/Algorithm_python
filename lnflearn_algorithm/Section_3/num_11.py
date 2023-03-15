'''Num_11: Palindrome'''
import sys
sys.stdin=open('input.txt', 'r')
a = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(7):
    for j in range(3):
        temp1 = a[i][j:j+5]
        # temp2 = a[j:j+5][i] 2차원 리스트에서 가로로 슬라이싱 하는 방법은 없음
        if temp1 == temp1[::-1]:
            cnt += 1
# for ~ else 문 사용
        for k in range(2): # 슬라이싱을 사용할 수 없으므로 양 끝단을 비교
            if a[j][i+k] ==  
        