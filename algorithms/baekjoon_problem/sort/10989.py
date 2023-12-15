import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
nums = []
for _ in range(n):
    temp = int(input())
    nums.append(temp)
# Counting Sort 구현 -> Timeover

# count = [0]*(max(nums)+1)

# for i in range(len(nums)):
#     count[nums[i]] += 1
# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i)

# Insertion Sort 구현 -> Timeover

# for i in range(1, len(nums)):
#     for j in range(i, 0, -1):
#         if nums[j-1] > nums[j]:
#             nums[j-1], nums[j] = nums[j], nums[j-1]
# for x in nums:
#     print(x)

def quick_sort_2(array):
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행, 전체 리스트 반환
    return quick_sort_2(left_side) + [pivot] + quick_sort_2(right_side)

result = quick_sort_2(nums)
for x in result:
    print(x)