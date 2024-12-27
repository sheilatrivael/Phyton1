import check
def describe_string(s: str, c: str) -> int:
  """
  Returns the number of characters in s
  minus the non-negative index of the
  rightmost occurrence of c
  plus the number of c occurrences in the string.
  
  Requires: len(c) == 1
  
  Examples:
     describe_string("", 'c') => 1
     describe_string("banana", 'c') => 7
     describe_string("banana", 'a') => 4
  """
  
  if len(s) == 0:
    return 1
  
  right_most_index = s.rfind(c) #will return -1 if c is not in s
  count = s.count(c)
  
  return len(s) - right_most_index + count
  pass

#Test
check.expect("Test 0", describe_string("", 'c'), 1)
check.expect("Test 1", describe_string("banana", 'c'), 7) 
check.expect("Test 2", describe_string("banana", "a"), 4)
check.expect("Test 3", describe_string("banana", "n"), 4) 