test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    lst = list(map(int,input().split()))
    lst.sort()
    start = 0
    ans = "YES"

    for i in range(n-1):
        if abs(lst[i]-lst[i+1]) <= 1:
            start += 1

    if start == n-1:
        print("YES")
    else:
        print("NO")
    

