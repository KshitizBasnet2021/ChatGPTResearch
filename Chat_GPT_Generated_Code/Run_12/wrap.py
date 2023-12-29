#wrap.py
#
#Yes, there is a bug in the provided code. The bug occurs when the length of the text is exactly equal to the number of columns. In this case, the code will enter an infinite loop because the condition `len(text) > cols` will always be true.
#
#To fix this bug, we can modify the condition to `len(text) >= cols`. This way, the loop will exit when the length of the remaining text is less than or equal to the number of columns.
#
#Here is the fixed code:
#
#```python
def wrap(text, cols):
    lines = []
    while len(text) >= cols:
        end = text.rfind(' ', 0, cols + 1)
        if end == -1:
            end = cols
        line, text = text[:end], text[end:]
        lines.append(line)
#
    lines.append(text)
    return lines
#```
#
#With this fix, the code will correctly handle cases where the length of the text is equal to the number of columns.
#
#
#