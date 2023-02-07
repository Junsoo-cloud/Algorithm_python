'''Num_1'''
N, K = map(int, input().split())
# map(function, iterable)
arrs = []
for i in range(1, N+1):
    if N % i == 0:
        arrs.append(i)
if arrs[K-1]:
    print(arrs[K-1])
else:
    print(-1)

# 강의 풀이 
N, K = map(int, input().split())
cnt = 0
for i in range(1, N+1):
    if N % i == 0:
        cnt += 1
    if cnt == K:
        print(i)
        break
else:
    print(-1)

    
# map()의 활용을 잘 해야 .. & split() 까지

