import check
def my_count(s: str, char: str) -> int:
  '''
  Returns the number of occurrences of char in s
  without using the string or list method count.
  
  Requires:
     len(char) == 1
  
  Examples:
     my_count("", "c") => 0
     my_count("banana", "a") => 3
  '''
  ct = 0
  for letter in s:
    if letter == char:
      ct += 1
  return ct
  
  pass

check.expect("Test 2", my_count("banana", "a"), 3)
check.expect("Test 1", my_count("", "c") , 0)