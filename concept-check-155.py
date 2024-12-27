import math
def stirling(n: int) -> float:
  """
  Returns an approximation to n! according to Stirling's formula
  
  Requires: 
     0 < n
  
  Examples:
     stirling(1) => 0.9221370088957891
     stirling(4) => 23.506175132893294
  """
  ##YOUR CODE GOES HERE
  factorial = math.sqrt(2*math.pi*n) * ((n/math.e)**n)
  return factorial
  pass

stirling(1)
stirling(2)
stirling(3)
stirling(4)