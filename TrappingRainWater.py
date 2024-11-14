# Given n non-negative integers representing an elevation map where the width of each bar is 1
# compute how much water it can trap after raining.


heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
max_height = max(heights)

# Initialize the matrix with '0's
matrix = [['0' for _ in range(len(heights))] for _ in range(max_height)]

# Fill in the '#' based on heights
for col, height in enumerate(heights):
    for row in range(max_height - height, max_height):
        matrix[row][col] = '#'

for row in matrix:
    print(row)

