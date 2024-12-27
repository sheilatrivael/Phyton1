import check
def sum_lasts(lol: list[list[int]]) -> int:
  """
  Returns the sum of all the last values 
  in the nonempty lists in lol
    
  Examples: 
     sum_lasts([]) => 0
     sum_lasts([[]]) => 0
     sum_lasts([[1,2],[],[7,8,9]]) => 11
  """
  
  sum = 0
  for L in lol:
    if L != []:
      sum += L[len(L)-1]
  return sum
  
check.expect("Ex 3", sum_lasts([[1,2],[],[7,8,9]]), 11)    
check.expect("Ex 1", sum_lasts([]), 0)
check.expect("Ex 2", sum_lasts([[]]), 0)