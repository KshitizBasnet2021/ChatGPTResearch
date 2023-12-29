#knapsack.py
#
#The provided code is missing the initialization of the memoization table for the base cases. To fix this, we can add a loop before the main loop to initialize the memoization table for the base cases.
#
#Here's the updated code:
#
def knapsack(capacity, items):
    from collections import defaultdict
    memo = defaultdict(int)
#
    # Initialize memoization table for base cases
    for j in range(1, capacity + 1):
        weight, value = items[0]
        if weight <= j:
            memo[1, j] = value
#
    for i in range(2, len(items) + 1):
        weight, value = items[i - 1]
#
        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]
#
            if weight <= j:
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )
#
    return memo[len(items), capacity]
#
#
#