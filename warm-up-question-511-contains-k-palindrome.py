import check
def contains_consecutive_k_palindrome(s: str, k: int) -> bool:
  """
  Returns whether or not s contains string of
  k consecutive letters that form a palindrome
  
  Requires: k > 0
  
  Examples:
     contains_consecutive_k_palindrome("", 1) => False
     contains_consecutive_k_palindrome("a", 1) => True
     contains_consecutive_k_palindrome("asdf", 2) => False
     contains_consecutive_k_palindrome("banana", 3) => True
  """
  
  if (s == "") or (k > len(s)):
    return False
  if (len(s) == 1):
    return True
  
  for i in range(k+1):   #for banana, len(s) = 6, 
    sliced = s[i:(i+k)]     #stop checking after s[i=3,6], so max range is 4 
    if sliced == sliced[::-1]:
      return True
  else:
    return False
  pass


check.expect("Test 0", contains_consecutive_k_palindrome("", 1), False)
check.expect("Test 1", contains_consecutive_k_palindrome("a", 1), True)
check.expect("Test 2", contains_consecutive_k_palindrome("asdf", 2), False)
check.expect("Test 3", contains_consecutive_k_palindrome("banana", 3), True)
check.expect("Test 4", contains_consecutive_k_palindrome("aba", 3), True)
check.expect("Test 5", contains_consecutive_k_palindrome("racecar", 7), True)
check.expect("Test 6", contains_consecutive_k_palindrome("madam", 5), True)
check.expect("Test 7", contains_consecutive_k_palindrome("madam", 10), False)