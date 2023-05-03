from collections import defaultdict, deque

n, m = map(int, input().split())
a, b = map(int, input().split())
graph = defaultdict(list)
parent = {}
queue = deque([a])
parent[a] = None


for _ in range(m):
    src,dst = map(int, input().split())
    graph[src].append(dst)
    graph[dst].append(src)
print(graph)

while queue:
    node = queue.popleft()
    for neighbour in graph[node]:
        if neighbour not in parent:
            queue.append(neighbour)
            parent[neighbour] = node

if b in parent:
    path = [b]
    while path[-1] != a:
        path.append(parent[path[-1]])

    print(len(path)-1)
    print(*reversed(path))

else:
    print(-1)
