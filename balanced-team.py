n = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = 0
i = 0
j = 0
 
while i < n:
    while (lst[i]-lst[j]) > 5:
        j += 1
    ans = max(ans,i-j+1)
    i += 1
    
print(ans)