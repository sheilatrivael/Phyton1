import check
def skip_letters(s: str, k: int) -> str:
  """
  Returns every kth letter of s in a string
  starting from the first character
  
  Requires: k > 0
  
  Examples:
     skip_letters("", 3) => ""
     skip_letters("a", 3) => "a"
     skip_letters("banana", 2) => "bnn"
  """

  ans = ""
  if (s != ""):
    ans += s[0:: k]
  return ans
  pass
  
check.expect("Test 0", skip_letters("", 3), "")
check.expect("Test 1", skip_letters("a", 3), "a")
check.expect("Test 2", skip_letters("banana", 2), "bnn")
check.expect("Test 3", skip_letters("myday", 1), "myday")
check.expect("Test 4", skip_letters("meltdown", 3), "mtw")