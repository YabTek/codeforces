n,m = map(int,input().split())
first_lst = list( map(int,input().split()))
second_lst = list( map(int,input().split()))

count = 0
ans = []

for i in range(m):
    while count < n and  first_lst[count] < second_lst[i]: 
        count += 1
    ans.append(count)
print(*ans)