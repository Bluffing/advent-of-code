grid = []
with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))


def is_cool(arr):
    s = "".join(arr)
    return s.count("MAS") + s.count("SAM") > 0


total = 0
for x in range(1, len(grid) - 1):
    for y in range(1, len(grid) - 1):
        # (/)
        t = grid[x - 1][y - 1] + grid[x][y] + grid[x + 1][y + 1]
        if not is_cool(t):
            continue

        # (\)
        t = grid[x - 1][y + 1] + grid[x][y] + grid[x + 1][y - 1]
        if is_cool(t):
            total += 1

print(total)
