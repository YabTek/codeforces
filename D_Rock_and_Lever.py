from collections import defaultdict
n = int(input())
graph = defaultdict(list)
for i in range(1,n+1):
    row = list(map(int, input().split()))
    for j in range(1,len(row)+1):
        graph[i].append((j, row[j-1]))
print(graph)



# from collections import defaultdict
# import math

# test_cases = int(input())

# for _ in range(test_cases):
#     n = int(input())
#     nums = list(map(int,input().split()))
#     d = defaultdict(int)

#     for num in nums:
#         d[int(math.log(n,2))] += 1
#     print(d)