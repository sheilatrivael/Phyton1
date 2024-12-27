import check
def sum_integers(t: tuple) -> int:
  """
  Returns the sum of all integers in t
  
  Examples:
     sum_integers(()) => 0
     sum_integers(("hi", 5.4, True)) => 0
     sum_integers((2, "apple", 4, 6, 8, (1,), "23")) => 20
  """
  
  tot = 0
  for i in range(len(t)):  
    if type(t[i]) == int:
      tot += t[i]
  return tot
  pass


check.expect("Test 0", sum_integers(()), 0)
check.expect("Test 1", sum_integers(("hi", 5.4, True)), 0)
check.expect("Test 2", sum_integers((2, "apple", 4, 6, 8, (1,), "23")), 20)