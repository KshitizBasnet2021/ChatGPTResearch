#mutation_1_line_no_8_ASR.py
#
#Yes, there is a bug in the provided code. The bug is in the line `total -= disk_usage(childpath)`. This line subtracts the disk usage of each child directory from the total, but it should be adding the disk usage instead.
#
#Here's the corrected code:
#
import os
#
def disk_usage(path):
  total = os.path.getsize(path)
  if os.path.isdir(path):
    for filename in os.listdir(path):
      childpath = os.path.join(path, filename)
      total += disk_usage(childpath)
#
  print ('{0:<7}'.format(total), path)
  return total
#
#
#