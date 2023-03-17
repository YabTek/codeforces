N = int(input())

for _ in range(N):

    n , m = map(int, input().split())
    original = input()
    original = '0' + original + '0'
    copy = list(original)
    cur = original
    prev = ''
    for _ in range(m):
        if prev == cur:
            break 
        for i in range(1, n + 1):

            if original[i] == '0':
                if int(original[i - 1 ]) + int(original[i + 1]) == 1:
                    copy[i] = '1'
        prev = original
        original = ''.join(copy)
        cur = original
    print(original[1:n + 1])

