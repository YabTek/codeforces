from collections import defaultdict
 
n = int(input())
 
for _ in range(n):
    ans = 'Yes'
    size = int(input())
    number = list(map(int,input().split()))
    string = list(input())
    d = defaultdict(int)
 
    for num,char in zip(number,string):
        if num in d:
            if d[num] != char:
                ans = 'No'
        else:
            d[num] = char
    print(ans)