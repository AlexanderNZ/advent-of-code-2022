def find_word(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    count = 0

    def check_direction(x, y, dx, dy):
        for i in range(word_len):
            if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] != word[i]:
                return False
            x += dx
            y += dy
        return True

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == word[0]:
                # Check all 8 possible directions
                if check_direction(r, c, 0, 1):  # Horizontal right
                    count += 1
                if check_direction(r, c, 0, -1):  # Horizontal left
                    count += 1
                if check_direction(r, c, 1, 0):  # Vertical down
                    count += 1
                if check_direction(r, c, -1, 0):  # Vertical up
                    count += 1
                if check_direction(r, c, 1, 1):  # Diagonal down-right
                    count += 1
                if check_direction(r, c, 1, -1):  # Diagonal down-left
                    count += 1
                if check_direction(r, c, -1, 1):  # Diagonal up-right
                    count += 1
                if check_direction(r, c, -1, -1):  # Diagonal up-left
                    count += 1

    return count

# Read the content of the file
with open('input.txt', 'r') as file:
    content = file.read().splitlines()

# Convert the content into a grid
grid = [list(line) for line in content]

# Find all instances of the word "XMAS"
word = "XMAS"
count = find_word(grid, word)

# Print the result
print(f"The word '{word}' appears {count} times in the word search.")