n,m = map(int,input().split())
lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
ans = []
 
i = 0
j = 0
while i < n and j < m:
    if lst1[i] < lst2[j]:
        ans.append(lst1[i])
        i += 1
    else:
        ans.append(lst2[j])
        j += 1
        
while i < n:
    ans.append(lst1[i])
    i += 1
while j < m:
    ans.append(lst2[j])
    j += 1
 
print(*ans)