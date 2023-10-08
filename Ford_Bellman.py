n, m = map(int, input().split())
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

def bellman_ford():
    distance = [float('inf')] * n
    distance[0] = 0

    for _ in range(n - 1):
        for a, b, c in edges:
            if distance[a - 1] + c < distance[b - 1]:
                distance[b - 1] = distance[a - 1] + c

    for _ in range(n - 1):
        for a, b, c in edges:
            if distance[a - 1] + c < distance[b - 1]:
                distance[b - 1] = -30000

    return distance


ans = bellman_ford()

for dist in ans:
    if dist == float('inf'):
        print(30000, end=' ')
    else:
        print(dist, end=' ')
