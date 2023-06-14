test_cases = int(input())

for _ in range(test_cases):
    chessboard = []
    max_sum = 0
    directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]

    n, m = map(int, input().split())

    for _ in range(n):
        row = list(map(int, input().split()))
        chessboard.append(row)

    for i in range(n):
        for j in range(m):
            cur_sum = chessboard[i][j]

            for dx,dy in directions:
                nx = i + dx
                ny = j + dy

                while 0 <= nx < n and 0 <= ny < m:
                    cur_sum += chessboard[nx][ny]
                    nx += dx
                    ny += dy
            max_sum = max(max_sum, cur_sum)

    print(max_sum)


