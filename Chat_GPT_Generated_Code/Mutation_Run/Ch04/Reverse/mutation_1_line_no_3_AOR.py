def reverse(S, start, stop):
  """Reverse elements in implicit slice S[start:stop]."""
  if start < stop + 1:
    S[start], S[stop-1] = S[stop-1], S[start]  # swap first and last
    reverse(S, start+1, stop-1)                # recur on rest
