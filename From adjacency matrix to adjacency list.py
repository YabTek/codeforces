n = int(input())

for i in range(1,n+1):
    lst = []
    row = list(map(int, input().split()))
    for j in range(1,len(row)+1):
        if row[j-1] == 1:
           lst.append(j)
    print(len(lst),*lst)