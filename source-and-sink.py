n = int(input())

rows = set()
cols = set()
sink = []
source = []

for i in range(1,n+1):
    row = list(map(int, input().split()))
    for j in range(1,len(row)+1):
        if row[j-1] == 1:
            rows.add(i)
            cols.add(j)

for i in range(1,n+1):
    if i in rows and i not in cols:
        source.append(i)
    elif i in cols and i not in rows:
        sink.append(i)
    elif i not in rows and i not in cols:
        sink.append(i)
        source.append(i)

print(len(source),*source)
print(len(sink),*sink)
