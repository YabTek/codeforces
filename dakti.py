n = int(input())
for _ in range(n):
    lst = list(map(str,input().split()))
    ans = []
    d = {}
    for word in lst:
        for char in word:
            if char.isdigit():
                d[int(char)] = word
    temp = sorted(d)
    for num in temp:
        ans.append(d[num])
   
    temp = ' '.join(ans)
    final  = ''.join([i for i in temp if not i.isdigit()])
 
   
    print(final)