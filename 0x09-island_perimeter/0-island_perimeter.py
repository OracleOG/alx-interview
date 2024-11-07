def island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Start with a potential contribution of 4
                perimeter += 4

                # Check for neighboring land cells
                if i > 0 and grid[i - 1][j] == 1:  # Land above
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # Land below
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Land to the left
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:  # Land to the right
                    perimeter -= 1

    return (perimeter)

