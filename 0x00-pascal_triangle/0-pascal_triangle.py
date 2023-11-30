#!/usr/bin/python3
"""
returns a list of lists of integers representing the Pascal’s triangle of n
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): Number of rows to generate.

    Returns:
        list of lists: Pascal's Triangle up to the nth row.
    """
    # Check if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate the remaining rows
    for i in range(1, n):
        # Each row starts and ends with 1
        row = [1]

        # Calculate the values in the middle of the row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        # Each row ends with 1
        row.append(1)

        # Append the row to the triangle
        triangle.append(row)

    return triangle
