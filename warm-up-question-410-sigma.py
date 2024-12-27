import check
def sigma(n: int) -> int:
  """
  Returns sum of all positive integer divisors of n
  
  Requires: 0 < n
  
  Examples:
     sigma(1) => 1
     sigma(6) => 12
  """ 
  
  sum = 0
  d = 1
  while (d <=n):
    if (d != 0) and (n % d == 0):
      sum = sum + d
    d += 1
  else:
    return sum
  
  pass

check.expect("Test1", sigma(1), 1)
check.expect("Test2", sigma(2), 3)
check.expect("Test3", sigma(3), 4)
check.expect("Test4", sigma(4), 7)
check.expect("Test5", sigma(5), 6)
check.expect("Test6", sigma(6), 12)