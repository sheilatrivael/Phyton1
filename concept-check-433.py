import check
def all_same_type(t: tuple) -> bool:
  """
  Returns True if and only if each element of t has the same type 
  and False otherwise.
  
  Examples:
     all_same_type(()) => True
     all_same_type((2, 5, 3)) => True
     all_same_type((2, 'R', 4.56)) => False
  """
  if len(t) == 0:
    return True
  
  reference = type(t[0])
  for i in range(1, len(t)):
    if type(t[i]) != reference:
      return False
  return True
  pass

check.expect("Test 1", all_same_type(()), True)
check.expect("Test 2", all_same_type((2, 5, 3)), True)
check.expect("Test 3", all_same_type((2, 'R', 4.56)), False)