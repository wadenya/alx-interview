#!/usr/bin/python3
"""
Minimum Operations
"""

def minOperations(n):
    if n <= 0:
        return 0

    # Init an array to store the minimum operations needed for each numb
    dp = [float('inf')] * (n + 1)

    # Base case: 0 operations needed to reach 1 H
    dp[1] = 0

    # Iterate from 2 to n and fill in the dp array
    for i in range(2, n + 1):
        # Check if i is divisible by any j (2 <= j <= i)
        for j in range(2, i + 1):
            if i % j == 0:
                # Copy All and Paste j times
                dp[i] = min(dp[i], dp[j] + i // j)

    # Return the minimum operations needed for n
    return dp[n] if dp[n] != float('inf') else 0
