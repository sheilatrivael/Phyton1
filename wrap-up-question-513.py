import check
def sum_odd_squares(L: list[int]) -> int:
  """
  Returns the sum of squares of all odd elements in L
  
  Examples:
     sum_odd_squares([]) => 0
     sum_odd_squares([1, 2, 3]) => 10
     sum_odd_squares([2, 4, 6, 8]) => 0
  """
  
  ans = 0
  for pos, i in enumerate(L):
    if i % 2 != 0: #check for odd numbers
      ans += (i**2)
  return ans  
  pass

check.expect("Test 1", sum_odd_squares([]), 0)
check.expect("Test 2", sum_odd_squares([1, 2, 3]), 10)
check.expect("Test 3", sum_odd_squares([2, 4, 6, 8]), 0)