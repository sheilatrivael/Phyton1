import check
def intersection(L: list, M: list) -> list:
  """
  Returns a list of common elements in L and M
  
  Requires: L and M do not contain duplicates
  
  Examples:
     intersection([1, 2, 3], []) => []
     intersection([1, 2, 3], [2, 99, 1]) => [1, 2]
  """
  
  ans = []
  for i in L:
    for f in M:
      if i == f:
        ans += [i]
  return ans
  pass

check.expect("Test 1", intersection([1, 2, 3], []), [])
check.expect("Test 2", intersection([5, 6], [5, 6]), [5, 6])
check.expect("Test 3", intersection([1, 2, 3], [2, 99, 1]), [1, 2])