# import sys
# sys.stdin=open('input.txt', 'r')
# A, B = [], []

# N, M = map(int, input().split())

# for row in range(N):
#     row = list(map(int, input().split()))
#     A.append(row)

# for row in range(N):
#     row = list(map(int, input().split()))
#     B.append(row)
    
# for row in range(N):
#     for col in range(M):
#         print(A[row][col] + B[row][col], end=' ')
#     print()

import sys
sys.stdin=open('input.txt', 'r')
n = 9
matrix = [list(map(int, input().split())) for _ in range(n)]
res = -2147000000
for i in range(n):
    for j in range(n):
        if res < matrix[i][j]:
            res = matrix[i][j]
            x = i+1
            y = j+1
print(res)
print(x, y)