import check
def my_equals(S: set, T: set):
  """
  Returns True if S and T are equal and False otherwise
  
  Examples:
     my_equals(set(), set()) => True
     my_equals(set(), {1}) => False
     my_equals({1}, set()) => False
  """

  if S.issubset(T) and S.issuperset(T):
    return True
  else:
    return False
  pass

check.expect("Test 1", my_equals(set(), set()), True)
check.expect("Test 2", my_equals(set(), {1}), False)
check.expect("Test 2", my_equals({1}, set()), False)