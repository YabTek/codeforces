n = int(input())
lst =list(map(int,input().split()))
start = 0
count = 0
for i in range(1,len(lst)):
    part = lst[start:i]
    if lst[i] > max(part) or lst[i] < min(part):
        count+=1
print(count)