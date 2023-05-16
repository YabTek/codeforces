from collections import defaultdict,deque

def parallelCourses(n, prerequisites):
    # Write your code here.
    
    graph = defaultdict(list)
    in_coming = defaultdict(int)
    queue = deque()
    ans = 0
    node_count = 0

    for a,b in prerequisites:
        graph[a].append(b)
        in_coming[b] += 1
    
    for i in range(1,n+1):
        if in_coming[i] == 0:
            queue.append(i)


    while queue:
        node_count += len(queue)

        for _ in range(len(queue)):
            node = queue.popleft()

            for neighbour in graph[node]:
                in_coming[neighbour] -= 1

                if in_coming[neighbour] == 0:
                    queue.append(neighbour)
            
        ans += 1

    if node_count == n:
        return ans
    return -1
        
    
