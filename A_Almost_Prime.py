num = int(input())

def findPrime(num):
    d = 2
    factors = []
    while d*d <= num:
        while num % d == 0:
            num //= d
            factors.append(d)
        d += 1
    if num > 1:
        factors.append(num)

    if len(set(factors)) == 2:
        return 1
    else:
        return 0

ans = 0
for n in range(1,num+1):
    ans += findPrime(n)

print(ans)

