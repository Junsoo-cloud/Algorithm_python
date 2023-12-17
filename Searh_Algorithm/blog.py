import sys
sys.stdin=open('input.txt', 'r')
arr_num = []
arr_left = []
for _ in range(10):
    arr_num.append(int(input()))
for i in range(10):
    x = (arr_num[i] % 42)
    if x not in arr_left:
        arr_left.append(x)
print(len(arr_left))