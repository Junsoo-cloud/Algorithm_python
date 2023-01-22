# Deepcopy Vs Shallocopy

# list	mutable 한 순서가 있는 객체 집합	-> mutable
# set	mutable 한 순서가 없는 고유한 객체 집합	-> mutable
# dict	key와 value가 맵핑된 객체, 순서 없음	-> mutable
# bool	참,거짓	-> immutable
# int	정수	-> immutable
# float	실수	immutable
# tuple	immutable 한 순서가 있는 객체 집합	i-> mmutable
# str	문자열	immutable
# frozenset	immutable한 set	-> immutable


import copy

# 그냥 copy

list_01 = [1,2,3]
list_02 = list_01

list_01[1] = 9
print(list_01, list_02)

for id_1 in list_01:
    print(id(id_1))
for id_2 in list_02:
    print(id(id_2))
    
print()

# Shallocopy : 1차원 배열은 id 값이 다르지만, 다차원 배열은 그렇지 못함
# deepcopy : 다차원 배열까지 id 값 다름

