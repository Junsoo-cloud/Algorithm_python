'''Num_2'''

T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    arrs = list(map(int, input().split()))
    arrs = arrs[s-1:e]
    arrs.sort()
    print(t+1, arrs[k-1])

