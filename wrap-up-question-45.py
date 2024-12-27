import check
def num_a(s: str) -> int:
  """
  Returns the number of 'a' characters in s
  """
  pos = 0
  ct = 0
  while (s != "") and (pos < len(s)):
    if s[pos] == 'a':
      ct += 1
    pos += 1
  return ct
  pass  
    

check.expect("Test 0", num_a(""), 0)  
check.expect("Test 0", num_a("day6"), 1)  
check.expect("Test 1", num_a("apple"), 1)  
check.expect("Test 2", num_a("avocado"), 2)
check.expect("Test 3", num_a("banana"), 3)