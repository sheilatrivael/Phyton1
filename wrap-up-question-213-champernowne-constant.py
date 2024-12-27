import check
def champernowne_constant(n: int) -> str:
  """
  Returns Chapernowne's Constant up to and include n
  as a string "0.1234567891011....n"
  
  Requires: n >= 1
  
  Examples:
     champernowne_constant(1) => "0.1"
     champernowne_constant(12) => "0.123456789101112"
  """
  
  ans = "0.1"
  a = 1
  while (1 <= a) and (a != n):
    ans = ans + str(a+1)
    a = a + 1
  return ans
  pass

check.within("1", champernowne_constant(1), "0.1", 0.00001)
check.within("3", champernowne_constant(3), "0.123", 0.00001)
check.within("9", champernowne_constant(9), "0.123456789", 0.00001)
check.within("10", champernowne_constant(10), "0.12345678910", 0.00001)
check.within("12", champernowne_constant(12), "0.123456789101112", 0.00001)