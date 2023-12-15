import sys
sys.stdin = open('input.txt', 'r')
n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()  # 오름차순 정렬
B.sort(reverse = True)  # 내림차순 정렬

# 첫번째 인덱스부터 확인하며, 최대 K 번 비교
for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break
print(sum(A))