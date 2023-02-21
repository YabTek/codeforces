n,k = map(int,input().split())
lst = list( map(int,input().split()))
lst.sort()

if k > 0 and k < len(lst) and lst[k-1] == lst[k]:
    print(-1)
elif k == 0 and lst[0] == 1:
    print(-1)
elif k == 0 and lst[0] != 1:
    print(1)
else:
    print(lst[k-1])

