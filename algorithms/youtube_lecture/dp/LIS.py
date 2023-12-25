import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = list(map(int, input().split()))
d = [1]*(n)
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            d[i] = max(d[i], d[j]+1)
print(max(d))


# max를 안쓰는 coding 도 필요할듯 -> O(n) 소요하니까 시간적으로 손해인 거 같은 느낌
