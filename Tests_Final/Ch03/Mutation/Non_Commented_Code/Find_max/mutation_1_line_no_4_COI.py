def find_max(data):
  biggest = data[0]
  for val in data:
    if not (val > biggest):
      biggest = val
  return biggest
