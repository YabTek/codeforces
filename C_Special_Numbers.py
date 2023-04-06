test_cases = int(input())

for _ in range(test_cases):
    n,k = map(int,input().split())
    i = 0
    ans = 0
    while k>0:
        if (k&1) == 1:
            ans += n**i
        i += 1
        k = k>>1

    print(ans%(10**9+7))


    
