from collections import defaultdict

n = int(input())
planes = list(map(int,input().split()))
d = defaultdict(int)
ans = "NO"

for num in planes:
    d[num] = planes[num-1]

if len(d) >= 3:
    for a,b in d.items():
        if b in d and d[d[b]] == a:
            ans = "YES"
print(ans)


