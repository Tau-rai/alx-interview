#!/usr/bin/python3
"""
This module contains a function that computes the perimeter an an island
"""


def island_perimeter(grid):
    """Calculates the perimeter of an island

    Args:
        island (list): a list of integers
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    if rows > 100 or cols > 100:
        raise ValueError("Gid width and height must be < 100")

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter
