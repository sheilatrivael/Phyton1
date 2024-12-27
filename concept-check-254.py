def factorial(n: int) -> int:
  """
  Returns n!
  
  Requires: n >= 0
  
  Examples:
     factorial(0) => 1
     factorial(4) => 24
  """
  
  fac = 1
  multiplied_by = 1 
  while multiplied_by <= n:
    fac = fac * multiplied_by
    multiplied_by = multiplied_by + 1 
  return fac
  pass

factorial(0) #1
factorial(1) #1 
factorial(2) #2
factorial(5) #120
factorial(4) #24

"""
version 1
  fac = 1
  ans = n or 1
  while n > 1:
    fac = ans * (n-1)
    ans = fac #temporary value
    n = n - 1 #updating value of n
  return ans
  pass

version 2
"""
