import check
def my_max(L: list[int|float]|list[str]) -> int|float|str:
  """
  Returns the maximum of L.

  Requires: L is non-empty
  
  Examples:
     my_max([1, 2.1, 3]) => 3
     my_max(['oranges', 'apples', 'pears', 'bananas']) => 'pears'
  """
 

  current_max = L[0]
  for i in L:
    if current_max < i:
      current_max = i
  return current_max
  pass
  
  
check.expect("Test 1", my_max([1, 2.1, 3]), 3)
check.expect("Test 2", my_max(['oranges', 'apples', 'pears', 'bananas']), 'pears')