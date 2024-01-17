import sys
sys.stdin = open('input.txt', 'r')

string = list(input())
n = int(input())
pointer = len(string)
for _ in range(n):
    temp = sys.stdin.readline().rstrip()
    if temp[0] == "P":
        string.insert(pointer, temp[2:])
        pointer += 1
    if temp == "L" and pointer != 0:
        pointer -= 1
    if temp == "D" and pointer != len(string):
        pointer += 1
    if temp == "B" and pointer != 0:
        string.pop(pointer-1)
        pointer -= 1
print(''.join(string))


# insert, remove , pop(index) -> O(n) 시간복잡도 소요
# 따라서 O(1) 인 append, pop() 함수로 사용하려면 쪼개야함

