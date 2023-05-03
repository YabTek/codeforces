test_cases = int(input())

for _ in range(test_cases):
    ans = float("inf")
    n = int(input())
    nums = list(map(int,input().split()))

    for i in range(n):
        for j in range(i+1,n):
            ans = min(ans,nums[i] & nums[j])
    print(ans)

