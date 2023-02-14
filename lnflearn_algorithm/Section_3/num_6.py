'''num_6'''
import sys
sys.stdin=open("input.txt", "r")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
max_row_list = []
max_column_list = []
# 행의 합 구하기
for i in range(n):
    s1 = 0 # s1 = 행의 합
    max_row =  0
    for j in range(n):
        s1 += a[i][j] # 행의 합 구하기
    max_row_list.append(s1)
max_row = max(max_row_list) # 행의 합 리스트에서 최댓값 구하기
# 열의 합 구하기
for i in range(n):
    s2 = 0
    max_column = 0
    for j in range(n):
        s2 += a[j][i]
    max_column_list.append(s2)
max_column = max(max_column_list) # 열의 합 리스트에서 최댓값 구하기
# 대각선 합 구하기
s3 = s4 = 0
max_diagonal = 0
for i in range(n):
    s3 += a[i][i]
    s4 += a[i][n-i-1]
max_diagonal = max(s3, s4)

print(max(max_diagonal, max_column, max_row))