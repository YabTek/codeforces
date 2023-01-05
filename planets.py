from collections import Counter
test_cases = int(input())
 
for _ in range(test_cases):
    ans = 0
    size,cost = map(int,input().split())
    planets = list(map(int,input().split()))
    planet_count = Counter(planets)
    
    for planet,count in planet_count.items():
        if count <= cost:
            ans += count
        else:
            ans += cost
    print(ans)
            