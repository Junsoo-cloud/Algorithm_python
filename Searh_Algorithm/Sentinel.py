# 1-2 Sentinel Method(보초법)

# Sentinel = if key값이 array에 없다면, array마지막에 Sentinel을 추가해서 프로그램을 끝냄 -> cost를 낮추기 위해서

from typing import Any, Sequence
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
    
    