n = int(input())
lst = list(map(int,input().split()))
lst.sort()
 
if lst[0:n] != lst[n:2*n]:
    print(*lst)
else:
    print(-1)
 