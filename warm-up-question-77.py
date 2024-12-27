import check
def one_liner(n: int) -> int:
  '''
  Returns the sum of digits using one line of code
  
  Requires: n >= 0
  
  Examples:
     one_liner(0) => 0
     one_liner(114) => 6
  '''
  return sum(int(i) for i in str(n))

check.expect("Test 0", one_liner(0), 0)
check.expect("Test 1", one_liner(114), 6)