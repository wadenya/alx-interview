#!/usr/bin/python3
"""determines if all the boxes can be opened"""
def canUnlockAll(boxes):
    # Get the number of boxes
    n = len(boxes)

    # Initialize a list to track visited boxes
    visited = [False] * n

    # Start with the first box (box 0) and use a stack for DFS traversal
    stack = [0]

    # Depth-First Search (DFS) Algorithm
    while stack:
        # Pop the current box from the stack
        current_box = stack.pop()

        # Mark the current box as visited
        visited[current_box] = True

        # Iterate through keys in the current box
        for key in boxes[current_box]:
            # If the corresponding box hasn't been visited, add it to the stack
            if not visited[key]:
                stack.append(key)

    # Check if all boxes have been visited
    return all(visited)
