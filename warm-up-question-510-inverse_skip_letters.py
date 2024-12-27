import check
def inverse_skip_letters(s: str, k: int) -> str:
  """
  Returns a string with every kth letter 
  of s removed
  
  Requires: k > 0
  
  Examples:
     inverse_skip_letters("", 3) => ""
     inverse_skip_letters("a", 3) => ""
     inverse_skip_letters("banana", 2) => "aaa"
  """
  
  ans = ""
  if (s == "") or (len(s) == 1):
    return ans

  for i in range(len(s)):
    if (((i + 1) % k) != 0) and ((i+1) < len(s)):
      ans += s[i+1]
  return ans
  pass
 
check.expect("Test 0", inverse_skip_letters("", 3), "")
check.expect("Test 1", inverse_skip_letters("a", 3), "")
check.expect("Test 2", inverse_skip_letters("banana", 2), "aaa")
check.expect("Test 2", inverse_skip_letters("banana", 3), "anna")
check.expect("Test 3", inverse_skip_letters("myday", 4), "yda")
check.expect("Test 4", inverse_skip_letters("meltdown", 3), "eldon")
check.expect("Test 6", inverse_skip_letters("a", 1), "")
check.expect("Test 7", inverse_skip_letters("abcde", 5), "bcde") 