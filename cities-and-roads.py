n = int(input())
lst = []

for i in range(1,n+1):
    row = list(map(int, input().split()))
    for j in range(1,len(row)+1):
        if row[j-1] == 1:
           if sorted([i,j]) not in lst:
               lst.append([i,j])
print(len(lst))
    