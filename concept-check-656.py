import check
def contains_positive(t: tuple[int]) -> bool:
  '''
  Returns True if t contains a positive number and False otherwise.
  
  Examples:
     contains_positive(()) => False
     contains_positive((1,)) => True
     contains_positive((-1,)) => False
     contains_positive((-231, -234, -1231234, 5, -1235)) => True
  '''
  
  return any(x>0 for x in t)
  pass



check.expect("1", contains_positive(()), False)
check.expect("2", contains_positive((1,)), True)
check.expect("3", contains_positive((-1,)), False)
check.expect("4", contains_positive((-231, -234, -1231234, 5, -1235)), True)