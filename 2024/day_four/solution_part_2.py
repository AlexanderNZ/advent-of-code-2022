def find_x_mas_pattern(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    def check_x_mas_pattern(x, y):
        patterns = [
            ('M', 'A', 'S', 'M', 'S'),  # MAS forward
            ('S', 'A', 'M', 'S', 'M'),  # MAS backward
            ('M', 'A', 'S', 'S', 'M'),  # Forward MAS, backward SAM
            ('S', 'A', 'M', 'M', 'S'),  # Backward SAM, forward MAS
        ]
        for p in patterns:
            if (0 <= x < rows - 2 and 0 <= y < cols - 2 and
                grid[x][y] == p[0] and grid[x][y + 2] == p[4] and
                grid[x + 1][y + 1] == p[1] and
                grid[x + 2][y] == p[3] and grid[x + 2][y + 2] == p[2]):
                return True
        return False

    for r in range(rows - 2):
        for c in range(cols - 2):
            if check_x_mas_pattern(r, c):
                count += 1

    return count

# Read the content of the file
with open('input.txt', 'r') as file:
    content = file.read().splitlines()

# Convert the content into a grid
grid = [list(line) for line in content]

# Find all instances of the "X-MAS" pattern
count = find_x_mas_pattern(grid)

# Print the result
print(f"The 'X-MAS' pattern appears {count} times in the word search.")