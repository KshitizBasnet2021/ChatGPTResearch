#powerset.py
#
#The provided code is missing a closing parenthesis at the end. Here is the corrected code:
#
def powerset(arr):
    if arr:
        first, *rest = arr
        rest_subsets = powerset(rest)
        return [[first] + subset for subset in rest_subsets]
    else:
        return [[]]
#
#
#