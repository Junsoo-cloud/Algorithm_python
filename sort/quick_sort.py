array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:   # 정렬해야할 원소가 1개인 경우 종료
        return
    pivot = start   # 피벗은 첫 번째 원소
    left = start + 1   # 피벗 제외
    right = end
    while left <= right:  # 엇갈리면 탈출
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while (left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while (right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):   # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]
        quick_sort(array, start, right - 1)
        quick_sort(array, right + 1, end)
quick_sort(array, 0, len(array) - 1)

#  파이썬 장점을 살린 방식 (slicing, list comprehension)

def quick_sort_2(array):
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행, 전체 리스트 반환
    return quick_sort_2(left_side) + [pivot] + quick_sort_2(right_side)

print(quick_sort_2(array))