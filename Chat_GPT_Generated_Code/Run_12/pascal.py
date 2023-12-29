#pascal.py
#
#There is a bug in the provided code. When calculating the values for the current row, the code is checking if `c < r` to access the value of `upright`. However, it should be checking if `c < r - 1` since the index of `upright` is `c` in the previous row. 
#
#Here's the corrected code:
#
def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = []
        for c in range(0, r + 1):
            upleft = rows[r - 1][c - 1] if c > 0 else 0
            upright = rows[r - 1][c] if c < r - 1 else 0
            row.append(upleft + upright)
        rows.append(row)
#
    return rows
#
#Now the code should work correctly and generate the Pascal's triangle with `n` rows.
#
#
#