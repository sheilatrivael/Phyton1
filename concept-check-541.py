import check
def product(L: list[int]) -> int:
  """
  Returns the product of all elements in L
  
  Examples:
     product([]) => 1
     product([1,2,3]) => 6
  """
  
  answer = 1
  for pos in range(len(L)):
    answer = answer * L[pos]
  return answer
    
check.expect("Test1", product([]), 1)
check.expect("Test2", product([1,2,3]), 6)