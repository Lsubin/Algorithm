import sys
sys.setrecursionlimit(10**6)

n = int(input())
m = int(input())

visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]
cnt = 0

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, 1, visited)

for i in range(2,n+1):
    if visited[i]:
        cnt += 1

print(cnt)
