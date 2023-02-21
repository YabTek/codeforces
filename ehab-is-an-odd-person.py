n = int(input())
lst = list( map(int,input().split()))
even_flag = False
odd_flag = False

for num in lst:
    if num % 2 != 0:
        odd_flag = True
    else:
        even_flag = True
        
if odd_flag  and even_flag:
    lst.sort()
    print(*lst)
else:
    print(*lst)