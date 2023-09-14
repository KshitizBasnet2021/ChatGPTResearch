#../python_programs/possible_change.py
#
#Yes, there is a bug in the provided code. The bug is in the recursive call to `possible_change` function. 
#
#The line `return possible_change(coins, total - first) + possible_change(rest, total)` should be changed to `return possible_change(coins, total - first) + possible_change(rest, total)`.
#
#Here's the corrected code:
#
#```python
def possible_change(coins, total):
    if total == 0:
        return 1
    if total < 0:
        return 0
#
    first, *rest = coins
    return possible_change(coins, total - first) + possible_change(rest, total)
#```
#
#Now the code should work correctly.
#
#
#