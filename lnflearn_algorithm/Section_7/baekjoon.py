import sys
sys.stdin=open('input.txt', 'r')
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))