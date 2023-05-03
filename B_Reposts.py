from collections import defaultdict

n = int(input())
graph = defaultdict(list)
a,b,c = map(str,input().split())


d = defaultdict(list)
visited = set()
ans = 2

for _ in range(n):
    a,b,c = map(str,input().split())
    graph[c.lower()].append(a.lower())

def dfs(node):
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            ans += 1
            dfs(neighbour)
dfs(c)
print(ans)