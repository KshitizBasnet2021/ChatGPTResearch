#mutation_1_line_no_9_ASR.py
#
#There is a bug in the provided code. When calculating the total disk usage for a directory, the code subtracts the disk usage of each child from the total. However, this subtraction should only occur if the child is a directory. 
#
#To fix this bug, we need to add a condition to check if the child is a directory before subtracting its disk usage from the total. Here's the corrected code:
#
#```python
import os
#
def disk_usage(path):
  """Return the number of bytes used by a file/folder and any descendents."""
  total = os.path.getsize(path)                  # account for direct usage
  if os.path.isdir(path):                        # if this is a directory,
    for filename in os.listdir(path):            # then for each child:
      childpath = os.path.join(path, filename)   # compose full path to child
      if os.path.isdir(childpath):               # check if child is a directory
        total -= disk_usage(childpath)
#
  print ('{0:<7}'.format(total), path)           # descriptive output (optional)
  return total                                   # return the grand total
#```
#
#With this fix, the code will correctly calculate the disk usage for directories and files.
#
#
#