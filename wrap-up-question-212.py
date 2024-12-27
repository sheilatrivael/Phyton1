def sum_powers(b: int, n: int) -> int:
  """
  Returns 1 + b + ... + b^n
  
  Requires: n >= 0
  
  Examples:
     sum_powers(0, 0) => 1
     sum_powers(0, 100) => 1
     sum_powers(2, 3) => 15
  """
  
  power = n
  ans = 0 
  while 0 <= power <= n:
    ans = ans + (b**power)
    power = power - 1
  return ans  
  pass

sum_powers(0, 0) # 1
sum_powers(0, 100) # 1
sum_powers(2, 3) # 15