import check
def count_ending(t: tuple[int, ...], digit: int) -> int:
  """
  Returns the number of values in t
  that end with digit
  
  Requires: 0 <= digit <= 9
  
  Examples:
     count_ending((), 3) => 0
     count_ending((13,), 3) => 1
     count_ending((13, 11, 51, 12, 66, 64, 35, 7, 99999999), 1) => 2
  """
  pos = 0
  ct = 0
  while t != () and (pos < len(t)):
    if digit == (t[pos] % 10):
      ct += 1
    pos += 1
  return ct
  pass


check.expect("Test 1", count_ending((), 3), 0)
check.expect("Test 2", count_ending((13,), 3), 1)
check.expect("Test 3", count_ending((13, 11, 51, 12, 66, 64, 35, 7, 99999999), 1), 2)