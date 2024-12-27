import check
def sparse(s: str, pos: int) -> None:
  """
  Prints out letters of s from pos to the end one character per line

  Effects: 
     Prints to screen

  Examples:
     sparse("", 0) => None
     and nothing is printed to the screen

     sparse("can", 1) => None
     and the following is printed:
     a
     n
  """
  
 
  ans = ""
  for char in range(pos, len(s)):
    ans += s[char] + "\n"
  print(ans.rstrip()) #delete the extra newlines at the end

  pass


check.set_print_exact("a\nn")
check.expect("Test 2", sparse("can", 1) , None)

check.set_print_exact("")
check.expect("Test 1", sparse("", 0), None)