test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = 0

    i = 0
    while i < n:
        j = i
        temp = lst[i]
        while j < n and lst[i] * lst[j] > 0:
            temp = max(temp, lst[j])
            j += 1
        ans += temp
        i = j
    
    print(ans)

