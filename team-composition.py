test_cases = int(input())
for _ in range(test_cases):
    a, b = map(int, input().split())
    ans = min(a,b,(a+b)//4)
    print(ans)