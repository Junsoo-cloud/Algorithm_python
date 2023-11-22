from collections import deque
import sys
sys.stdin=open('input.txt', 'r')

def bfs(graph, start, visited):
    cnt = 0
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in range(vertex):
            if graph[i][0] == v:
                if not visited[graph[i][1]]:
                    queue.append(graph[i][1])
                    visited[graph[i][1]] = True
                    cnt += 1
    print(cnt)

node = int(input())
vertex = int(input())
graph = [list(map(int, input().split())) for _ in range(vertex)]
graph = deque(graph)
graph.appendleft([0,0])
graph = list(graph)
visited = [False]*node
bfs(graph, 1, visited)


