import check
def is_distinct(L: list) -> bool:
  """
  Returns True if elements in L are distinct and 
  False otherwise.
  
  Requires: Elements in L are immutable.
  
  Examples:
     is_distinct([]) => True
     is_distinct([1, 1, 3]) => False
  """
  
  S = set(L)
  if len(L) == len(S):
    return True
  else:
    return False
  pass

check.expect("Ex 1", is_distinct([]), True)
check.expect("Ex 2", is_distinct([1, 1, 3]), False)