#mutation_2_line_no_6_COI.py
#
#There is a bug in the provided code. When checking if a path is a directory, the code uses `os.path.isdir(path)`. However, this check should be done before getting the size of the path using `os.path.getsize(path)`. 
#
#Here's the fixed code:
#
#```python
import os
#
def disk_usage(path):
  """Return the number of bytes used by a file/folder and any descendents."""
  if os.path.isdir(path):
    total = 0
    for filename in os.listdir(path):            # then for each child:
      childpath = os.path.join(path, filename)   # compose full path to child
      total += disk_usage(childpath)             # add child's usage to total
  else:
    total = os.path.getsize(path)                  # account for direct usage
#
  print ('{0:<7}'.format(total), path)           # descriptive output (optional)
  return total                                   # return the grand total
#```
#
#In the fixed code, the check for directory is done first, and if it is a directory, the code recursively calculates the total size of all its children. If it is not a directory, the code directly gets the size of the path.
#
#
#