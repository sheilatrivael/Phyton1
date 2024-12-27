import check
def even_product(t: tuple[int, ...]) -> int:
  """
  Returns the product of all even numbers in t
  
  Examples:
     even_product(()) => 1
     even_product((11,)) => 1
     even_product((11,2)) => 2
     even_product((2, 3, 4, 5, 6, 7, 8)) => 384
  """

  pos = 0
  ans = 1
  while t != () and (pos < len(t)):
    if t[pos] % 2 == 0:
      ans = (ans * int(t[pos]))
    pos += 1
  return ans
  pass



check.expect("Test 1", even_product(()), 1)
check.expect("Test 2", even_product((11,)), 1)
check.expect("Test 3", even_product((11,2)), 2)
check.expect("Test 4", even_product((2, 3, 4, 5, 6, 7, 8)), 384)