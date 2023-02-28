'''Num_9: Anagram(Hash)'''
import sys
from collections import defaultdict
sys.stdin=open('input.txt', 'r')
first = input()
second = input()
first_dict = defaultdict(int)
second_dict = defaultdict(int)
for x in first:
    first_dict[x] += 1
for y in second:
    second_dict[y] += 1
for key in first_dict.keys():
    if key in second_dict.keys():
        if first_dict[key] != second_dict[key]:
            print('NO')
            break
    else:
        print('NO')
        break

else:
    print('YES')