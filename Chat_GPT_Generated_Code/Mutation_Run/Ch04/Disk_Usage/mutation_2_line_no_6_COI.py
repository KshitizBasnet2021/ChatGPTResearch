import os

def disk_usage(path):
  """Return the number of bytes used by a file/folder and any descendents."""
  total = os.path.getsize(path)                  # account for direct usage
  if not (os.path.isdir(path)):
    for filename in os.listdir(path):            # then for each child:
      childpath = os.path.join(path, filename)   # compose full path to child
      total += disk_usage(childpath)             # add child's usage to total

  print ('{0:<7}'.format(total), path)           # descriptive output (optional)
  return total                                   # return the grand total
