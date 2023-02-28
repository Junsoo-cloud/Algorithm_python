'''Num_10: 최소힙'''
import sys
import heapq as hq
sys.stdin=open('input.txt', 'r')
n = int(input())
a = []
for _ in range(n):
    n = int(input())
    if n == 0:
        if len(a) != 0:
            print(hq.heappop(a)[1])
        else:
            print(0)
    else:
        hq.heappush(a, (-n, n))
# python heapq : 완전 이진 트리를 기반으로 함 
# heapq.heappush(heap, item)
# heapq.heappop(heap)
# heapq.heapify(x) : Linear List x -> heaqp (O(n): N)
# heapq.heapreplace(heap, item) : pop & push 동시에 함 , if heapq empty -> raise IndexError
