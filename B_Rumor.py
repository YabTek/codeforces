from collections import defaultdict, deque

n,m = map(int,input().split())
golds = list(map(int,input().split()))
friends = defaultdict(list)
visited = set()
queue = deque()
total = 0


for _ in range(m):
    a,b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(1,n+1):

    if i not in visited:
        min_ = golds[i-1]
        queue.append(i)

        while queue:
            node = queue.popleft()

            for neighbour in friends[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    min_ = min(min_,golds[neighbour-1])

        total += min_

print(total)



                    








    