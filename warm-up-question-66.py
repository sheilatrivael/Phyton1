import check
def sum_last_digits(L: list[int]) -> int:
  """
  Returns the sum of all last digits of L
  
  Examples:
     sum_last_digits([]) => 0
     sum_last_digits([1, 2, 3]) => 6
     sum_last_digits([15, 23, 44]) => 12
  """
  ans = 0
  for i in L:
    ans += (i % 10)
  return ans
  pass

check.expect("Test 1", sum_last_digits([]),  0)
check.expect("Test 2", sum_last_digits([1, 2, 3]),  6)
check.expect("Test 3", sum_last_digits([15, 23, 44]),  12)
check.expect("Test 3", sum_last_digits([151, 231, 441]),  3)