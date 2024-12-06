grid = []
with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))


def get_in_array(arr):
    s = "".join(arr)
    return s.count("XMAS") + s.count("SAMX")


total = 0
width = len(grid)

for n in range(width):
    # horizontal
    total += get_in_array(grid[n])

    # vertical
    total += get_in_array([grid[i][n] for i in range(width)])

    # diagonal (/) : bot right corner
    line = [grid[width - 1 - i][n + i] for i in range(width - n)]
    total += get_in_array(line)

    # diagonal (/) : top left corner
    if n != width - 1:  # dont double count the middle diagonal
        line = [grid[n - i][i] for i in range(n + 1)]
        total += get_in_array(line)

    # diagonal (\) : top right corner
    line = [grid[i][n + i] for i in range(width - n)]
    total += get_in_array(line)

    # diagonal (\) : bot left corner
    if n != 0:  # dont double count the middle diagonal
        line = [grid[n + i][i] for i in range(width - n)]
        total += get_in_array(line)

print(total)
