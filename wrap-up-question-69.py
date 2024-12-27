import check
def equidigital(m: int, n: int) -> bool:
  '''
  Returns True if m and n contain the same digits and False otherwise.
  
  Requires: m, n > 0
  
  Examples:
     equidigital(0, 0) => True
     equidigital(111111112222111, 21) => True
     equidigital(123, 432) => False
  '''
  #duplicate items are not allowed in sets 
  M = set(str(m)) #will only give 1 number once --> {1,2} for Test 2
  N = set(str(n))
  
  if M.difference(N) == set():
    return True
  else:
    return False

  
  pass

check.expect("Test 1", equidigital(0, 0), True)
check.expect("Test 2", equidigital(111111112222111, 21), True)
check.expect("Test 3", equidigital(123, 432), False)