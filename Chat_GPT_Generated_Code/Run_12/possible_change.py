#possible_change.py
#
#The provided code has a bug in the recursive calls. It should be calling `possible_change(rest, total - first)` instead of `possible_change(coins, total - first)`. Here's the corrected code:
#
#```python
def possible_change(coins, total):
    if total == 0:
        return 1
    if total < 0 or not coins:
        return 0
#
    first, *rest = coins
    return possible_change(rest, total - first) + possible_change(coins, total)
#```
#
#This fix ensures that the recursive calls are made with the remaining coins (`rest`) and the updated total (`total - first`).
#
#
#