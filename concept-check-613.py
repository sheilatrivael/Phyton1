import check
def almost_equal(S: set[int], T: set[int]) -> bool:
  """
  Returns True if S and T are almost equal and False otherwise
  
  Examples:
     almost_equal(set(), set()) => True
     almost_equal({1}, set()) => False
     almost_equal({2, 4, 6, 8}, {7, 5, 3}) => True
  """
  
  if len(S) == 0 and len(T) == 0:
    return True
  
  for i in S:
    if not ((i+1 in T) or (i-1 in T)):
      return False
  
  for i in T:
    if not ((i+1 in S) or (i-1 in S)):
      return False
  
  return True
  pass

check.expect("Ex 3", almost_equal({2, 4, 6, 8}, {7, 5, 3}), True)
check.expect("Ex 1", almost_equal(set(), set()), True)
check.expect("Ex 2", almost_equal({1}, set()), False)