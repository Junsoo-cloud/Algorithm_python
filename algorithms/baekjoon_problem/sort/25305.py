import sys
# Recursion Error 방지 - 재귀 한도 10000까지 풀어주기
sys.setrecursionlimit(10000)
n, k = map(int, input().split())
score = list(map(int, input().split()))

def quick_sort(array):    # quick_sort 구현
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(score)[-k])