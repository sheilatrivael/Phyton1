import check
import math

def euler(n: int) -> int:
  """
  Returns phi(n)
  
  Requires: 0 < n
  
  Examples:
     euler(1) => 1
     euler(6) => 2
     euler(7) => 6
     euler(10) => 4
  """
  x = n 
  y = 1
  sum = 0
  while (y <= x): 
    if math.gcd(x,y) == 1:
      sum += 1
    y += 1
  else:
    return sum
  
  
  pass

check.expect("Test1", euler(1), 1)
check.expect("Test1", euler(6), 2)
check.expect("Test1", euler(7), 6)
check.expect("Test1", euler(10), 4)