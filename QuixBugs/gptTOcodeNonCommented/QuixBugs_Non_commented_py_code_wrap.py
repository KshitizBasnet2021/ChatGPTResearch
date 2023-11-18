#wrap.py
#
#Yes, there is a bug in the provided code. If the length of the text is exactly equal to the number of columns, the code will enter an infinite loop because it will never find a space to split the text.
#
#To fix this bug, we can add a condition to check if the length of the text is less than or equal to the number of columns. If it is, we can simply append the remaining text to the lines list and break out of the loop.
#
#Here's the updated code:
#
def wrap(text, cols):
    lines = []
    while len(text) > cols:
        end = text.rfind(' ', 0, cols + 1)
        if end == -1:
            end = cols
        line, text = text[:end], text[end:]
        lines.append(line)
#
    if len(text) <= cols:
        lines.append(text)
#
    return lines
#
#
#