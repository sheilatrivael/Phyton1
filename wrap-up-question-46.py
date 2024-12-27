import check
def count_a(s: str) -> int:
  """
  Returns the number of 'a' characters in s
  
  Examples:
     count_a('') => 0
     count_a('abca') => 2
  """
  pos = 0
  ans = 0
  while pos < len(s):
    if s[pos] == 'a':
      ans += 1
    pos += 1
  return ans
  
check.expect("Test 0", count_a(''), 0)  
check.expect("Test 0", count_a("abca"), 2)  
check.expect("Test 1", count_a("apple"), 1)  
check.expect("Test 2", count_a("avocado"), 2)
check.expect("Test 3", count_a("banana"), 3)