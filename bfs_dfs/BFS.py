# bfs -> not recursion 
from collections import deque
import sys
sys.stdin=open('input.txt', 'r')

v = int(input())
# 정점(Vertex) input 받기
e = int(input())
# 간선(Edge) input 받기
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split()) # a번째 vertex의 연결된 b번 vertex를 리스트에 추가 -> 연결된 것 알 수 있음
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited):
    deq = deque([start]) # 시작 노드(1번) deq에 넣어주기
    cnt = 0
    visited[start] = True # 방문처리 하기
    while deq: # deq가 popleft 돼서 다 빌때까지 실행 -> recursion 으로 구현할 필요 x
        v= deq.popleft()
        for next_node in graph[v]: # 인접 노드 방문(bfs)
            if not visited[next_node]: # 방문하지 않았으면
                visited[next_node] = True # 방문처리 하고
                deq.append(next_node) # deq에 append 하여 bfs 진행
                cnt += 1
    return cnt
visited = [False]*(v+1)
print(bfs(graph, 1, visited))
