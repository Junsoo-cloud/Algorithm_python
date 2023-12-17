v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())  # a번째 노드와 연결된 b번째 노드
    graph[a].append(b)
    graph[b].append(a)
    # 무방향 그래프 구현
