from itertools import accumulate
n,k,q = map(int,input().split())
arr = [0]*200002
 
for _ in range(n):
    start,end = map(int,input().split())
    arr[start] += 1
    arr[end+1] -= 1
   
arr = list(accumulate(arr))
for i in range(len(arr)):
    if arr[i] < k:
        arr[i] = 0
    else:
        arr[i] = 1
arr = list(accumulate(arr))
    
for _ in range(q):
    start,end = map(int,input().split())
    if start == 0:
        print(arr[end])
    else:
        print(arr[end]-arr[start-1])
    