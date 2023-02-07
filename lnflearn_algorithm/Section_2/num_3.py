'''Num_3'''
# Brute-Force
import random
n, k = map(int, input().split())
print(n, k, type(n))
a = list(map(int, input().split()))
sets = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            sets.add(a[i] + a[j] + a[m])

sets = list(sets)
sets.sort(reverse=True)
print(sets[k-1])

# 집합 자료형은 sort 할 수 없음
# map 함수를 list로 묶는것도 잘 생가
# 브루트 포스로 구현하는 문제