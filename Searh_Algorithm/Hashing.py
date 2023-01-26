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
        '''return hash value of key'''
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
    
    def add(self, key:Any, value: Any) -> bool:
        hash = self.hash_value(key) # hash : hash value of inputed key
        p = self.table[hash] # hash value 
        
        while p is not None:
            if p.key == key: # already exsisted Node (p.key) == append key:
                return False # Fail append
            p = p.next # Make new Node & focus Next Node
            
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp # Make Node
        return True    # success append
                
    # def remove(self, key: Any) -> bool:
    #     '''remove element of key'''
    #     hash = self.hash_value(key)
    #     p = self.table[hash]
    #     pp = None
        
    #     while p is not None:
    #         if p.key == key:
    #             if pp is None:
    
    def dump(self) -> None:
        '''Dump Hash table'''
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end = '')
            while p is not None:
                print(f'    -> {p.key} ({p.value})', end = '')
                p = p.next
            print()
        
    
    
# Open Addressing(Closed Hashing)

