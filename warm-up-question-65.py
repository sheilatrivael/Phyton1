import check
def is_palindrome(s: str) -> bool:
  """
  Returns True if s is a palindrome and False otherwise
  
  Examples:
     is_palindrome("") => True
     is_palindrome("banana") => False
     is_palindrome("radar") => True
  """
  
  if s[::-1] == s:
    return True
  else:
    return False
  
  pass

check.expect("Test 1", is_palindrome(""),  True)
check.expect("Test 2", is_palindrome("banana"),  False)
check.expect("Test 3", is_palindrome("radar"),  True)
check.expect("Test 4", is_palindrome("racecar"), True)