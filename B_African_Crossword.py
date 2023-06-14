n, m = map(int, input().split())

grid = [input() for _ in range(n)]

encrypted_word = ""
for i in range(n):
    for j in range(m):
        letter = grid[i][j]
        if grid[i].count(letter) == 1 and [grid[k][j] for k in range(n)].count(letter) == 1:
            encrypted_word += letter

print(encrypted_word)
