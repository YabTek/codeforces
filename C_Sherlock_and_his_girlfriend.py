from collections import defaultdict
n = int(input())

d = defaultdict(list)
color = 1
d2 = defaultdict(int)

lst = []
for i in range(1,n+1):
    lst.append(2+i)

i = 2
while i*i <= lst[-1]:
    j = i*i
    while j <= lst[-1]:
        d[i].append(j)
        j += i
    i += 1
ans = []

for num in lst:
    if d[6
    ans.append(color)



print(d)
