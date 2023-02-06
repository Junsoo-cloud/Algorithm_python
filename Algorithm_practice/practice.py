def binary_seach(x, key):
    pl = 0
    pr = len(x) - 1
    while True:
        pc = (pl + pr) // 2
        if x[pc] == key:
            return 1
        elif x[pc] > key:
            pr = pc - 1
        elif pl > pr:
            return 0
        else:
            pl = pr + 1

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1]
n = int(input())
key_list = list(map(int, input().split()))  
key_list.sort()

m = int(input())
an_list = list(map(int, input().split()))

for i in an_list:
    print(binary_seach(key_list, i))
    
    def isPalindrome(self, s: str) -> bool:
    strs = []

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    strs = strs.join
    strs = list(strs)
    return strs == strs[::-1]