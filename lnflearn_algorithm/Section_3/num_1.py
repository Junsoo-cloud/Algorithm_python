'''Num_1 : Palindrome'''
n = int(input())
for i in range(n):
    s = input()
    s = s.lower()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print('No')
    else:
        print('Yes')