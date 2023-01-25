from __future__ import annotations
# Hashig : 데이터를 저장할 위치 = 인덱스 -> 간단한 연산으로 구할 수 있음
# 장점: 효과적으로 데이터 검색, 추가, 삭제 등 조작할 수 있음
# value % len(array) = hash value

# hash value == index / 새롭게 저장한 배열 == hash table


# hash collision -> n:1 (key:hash value) -> hash function을 사용해야 함 !
# -> 대처 방법 : 1. chaining, open hashing


# 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
# https://seongonion.tistory.com/23


# key(value of element) % (numbers of element) = hash value(Index of hash table)

a = [5,6,14,20,29,34,37,51,69,75]

hv_list = []

for i in a:
    hv = i % len(a)
    hv_list.append(hv)

    
print(hv_list)
    
# isinstance Method
# numbers = [1, 2, 3, 4, 2, 5]

# # check if numbers is instance of list
# result = isinstance(numbers, list)
# print(result)

# # Output: True


# Hash Collision(collision of bucket) -> Same hash value(code) ,  key : hash value = n : 1 

# -> 1. chaining,  2. open hashing

# Chaining : Use linked list 


from typing import Any, Sequence
import hashlib

class Node(object):
    '''Node of Hash, Single Bucket'''
    
    def __init__(self, key:Any, value: Any, next: Node) -> None:
        '''init'''
        
        self.key = key
        self.value = value
        self.next = next
        
        
class ChainHash(object):
    '''Hash Class with Hashing'''
    
    def __init__(self, capacity: int) -> None:
        
        self.capacity = capacity
        self.table = [None] * self.capacity
        
    def hash_value(self, key: Any) -> int:
        if isinstance(key, int): # isinstance method : isinstance(object, classinfo) -> bool 
            return key % self.capacity
        # key가 int가 아닌 경우도 return 하는 method들이 있는데 , 뭔말인지 몰라서 int형인것만 하겠다
        
    def search(self, key: Any) -> Any:
        '''return Key(input) is key '''
        
        hash = self.hash_value(key)
        p = self.table[hash] # p is index of hash table  (Node)
    
        while p is not None:
            if p.key == key:
                return p.value
            p = p.next
            
        return None

if __name__ == '__main__':
    is_num_1 = Node()
    