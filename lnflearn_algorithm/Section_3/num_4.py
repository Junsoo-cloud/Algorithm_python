'''Num_4 : O(n)에 대한 공부? 암기가 필요 -> 어떻게 풀어야하는지 방향성 중요'''




import sys
sys.stdin=open("input.txt", "r")
# Sol_1 -> just +, sort : O(n) = nlogn
n = int(input())
first = list(map(int, input().split()))
m = int(input())
second = list(map(int, input().split()))
res = first + second
res = sorted(res)
print(res)

# Sol_2 -> point1, 2 
n = int(input())
first = list(map(int, input().split()))
m = int(input())
second = list(map(int, input().split()))
res = []
p1=p2=0
while p1 < n and p2< m:
    if first[p1] <= second[p2]:
        res.append(first[p1])
        p1 += 1
    else:
        res.append(second[p2])
        p2 += 1
if p1 < n:
    res.append(first[p1:])
if p2 < m:
    res += second[p2:]
print(res)