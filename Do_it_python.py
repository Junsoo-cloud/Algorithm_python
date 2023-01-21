# 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    # parameter의 type , -> return하는 값

# 1. Search Algorithm

# 1-1 Linear Search

# 구현 해보기 (if문의 순서도 중요하다는 것을 깨달음)

from typing import Any, Sequence

def Linear_Search(x : Sequence, key : Any) -> int:
    
    i = 0
    while True:
        if i == len(x):
            return f'Not Found!'
        elif x[i] == key:
            return f'{i} is key index!'

        else:
            i += 1
            
if __name__ == "__main__":
    num = int(input("input Number of Array: "))
    arr = [None] * num
    
    for i in range(num):
        arr[i] = int(input(f"Input :arr[{i}] : "))
    
    key = int(input("Input Key: "))
    
    ls = Linear_Search(arr, key)
    
    print(ls)

# 1-2 Sentinel Method -> 내일 .. 