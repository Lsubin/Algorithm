import sys
sys.setrecursionlimit(10 ** 6)

n, m, r = map(int,sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]

visited = [0]*(n+1)
result = [0]*(n+1)

c = 1
def dfs(graph, v, visited):
    global c
    visited[v] = 1
    result[v] = c
    graph[v].sort(reverse=True)
    for i in graph[v]:
        if visited[i] == 0:
            c += 1
            dfs(graph, i, visited)
            

for i in range(m):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


dfs(graph, r, visited)

for i in range(1, n+1):
    print(result[i])