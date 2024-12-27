def sum_multiples(n: int, k: int) -> int:
  """
  Returns sum of all multiples of k <= n
  
  Requires: 0 < n, k
  
  Examples:
     sum_multiples(1, 1) => 1
     sum_multiples(14, 3) => 30
  """
  
  sum = 0
  mult = 1
  while (k*mult) <= n:
    sum = sum + (k*mult)
    mult = mult + 1
  else:
    return sum
  pass

sum_multiples(14, 3)