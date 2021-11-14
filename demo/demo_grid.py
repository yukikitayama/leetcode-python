grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

m = len(grid)
n = len(grid[0])
for row in range(m):
    for col in range(n):
        print(row * n + col)