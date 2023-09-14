#../python_programs/knapsack.py
#
#There is a bug in the provided code. The condition `if weight < j` should be `if weight <= j` in order to include items with weight equal to the remaining capacity of the knapsack.
#
#Here is the corrected code:
#
#```python
def knapsack(capacity, items):
    from collections import defaultdict
    memo = defaultdict(int)
#
    for i in range(1, len(items) + 1):
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
#```
#
#Now the code should work correctly.
#
#
#