test_cases = int(input())

def main():
    x = int(input())
    y = (x & (-1*x))
    
    if x == 1:
        return 3
    elif x & y > 0 and x ^ y > 0:
        return y
    else:
        if x & 1 == 1:
            return x-1
        else:
            return x+1
    
for _ in range(test_cases):
    print(main())