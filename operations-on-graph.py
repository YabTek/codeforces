from collections import defaultdict 

vertices = int(input())
operations = int(input())
graph = defaultdict(list)

for i in range(operations):
    lst = list(map(int, input().split()))

    if lst[0] == 2:
        print(*graph[lst[1]])
    else:  
        graph[lst[1]].append(lst[2])
        graph[lst[2]].append(lst[1])
        