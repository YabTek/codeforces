from collections import defaultdict

def isBipartite(graph):

    color = {}

    for i in range(len(graph)):
        if i not in color:
            stack = [(i,1)]
            
            while stack:
                node,prev_color = stack.pop()

                if node in color:
                    if color[node] != prev_color:
                        return ('NOT BICOLOURABLE.')
                else:
                    color[node] = prev_color
                    for neighbour in graph[node]:
                        stack.append((neighbour,(-1)*prev_color))
    return ('BICOLOURABLE.')

def takeInputs():
    while True:
        graph = defaultdict(list)

        node = int(input())
        if node == 0:
            return
        edge = int(input())

        
        for _ in range(edge):
            a,b = map(int,input().split())
            graph[a].append(b)
            graph[b].append(a)

        print(isBipartite(graph))


takeInputs()
