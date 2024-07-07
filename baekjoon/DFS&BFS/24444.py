import sys
sys.setrecursionlimit(10**6)
from collections import deque

n, m, r = map(int,sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]

visited = [0]*(n+1)

c = 1
def bfs(graph, start, visited):
    global c
    q = deque([start])
    visited[start] = 1
    while q:
        x = q.popleft()
        graph[x].sort()
        for i in graph[x]:
            if visited[i] == 0:
                c += 1
                visited[i] = c
                q.append(i)

for i in range(m):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(graph, r, visited)

for i in visited[1:]:
    print(i)
