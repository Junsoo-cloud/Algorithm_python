# Binary Search : Array sorted , Linear Search보다 빠르게 검색
import time
from typing import Any, Sequence






def bin_search(a: Sequence, key: Any) -> int:
    '''Sequence a -> Key (binary search)'''

    pl = 0
    pr = len(a) - 1
    

    while True:
        pc = (pr+pl)//2
        if a[pc] == key:
            return f'Found! in {pc}'
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            return 'Not Found!'

if __name__ == '__main__':
    num = int(input('Input numbers of element: '))
    x = [None] * num
    
    x[0] = int(input('x[0]: '))
    
    for i in range(1,num):
        x[i] = int(input(f'x[{i}]: '))
        if x[i] < x[i-1]:
            break
    key = int(input('Input Key : '))
    
    idx = bin_search(x,key)
    print(idx)
    
    
start_time = time.time()  
end_time = time.time()
print('time : ', end_time - start_time)
    
# Time complextiy & Space complexity

# Time complextiy : 실행하는데 필요한 시간 = O(max(f(n), g(n))) Big-O 표기법 
# Space complextiy : 메모리(기억 공간)와 파일 공간이 얼마나 필요한지를 평가

# 1-2 Sentinel Method(보초법)

# Sentinel = if key값이 array에 없다면, array마지막에 Sentinel을 추가해서 프로그램을 끝냄 -> cost를 낮추기 위해서
dasd
from typing import Any, Sequencewdad
import copy

def Linear_Search_with_Sentinel(x : Sequence, key : Any) -> int:
    
    input_array = copy.deepcopy(x)
    
    input_array.append(key)
    i = 0
    while True:
        if key == input_array[i]:
            return f'Found ! in {i}!'
        i += 1
        
        if i == len(x):
            return -1
        
if __name__ == "__main__":
    num = int(input("input Number of Array: "))
    arr = [None] * num
    
    for i in range(num):
        arr[i] = int(input(f"Input :arr[{i}] : "))
    
    key = int(input("Input Key: "))
    
    ls = Linear_Search_with_Sentinel(arr, key)
    
    if ls == -1:
        print('Not Found! Try again! ')
    
    
