import check

def analyze_string(s: str) -> None:
  """
  Prints to the screen:
  contains C characters, P spaces, and ends with 'E'.
  (including the period above) where:
  C is the length of s, 
  P is the number of spaces (' ') in s
  E is the last character in s.
  
  Effects:
     Prints to screen
  
  Examples:
     analyze_string("") => None
     and prints
     contains 0 characters, 0 spaces, and ends with ''.
  
     analyze_string("Bananas are ripe!") => None
     and prints
     contains 17 characters, 2 spaces, and ends with '!'.
  """
  
  characters = len(s)
  spaces = s.count(' ')
  if characters != 0:
    last = s[-1]
    print(f"contains {characters} characters, {spaces} spaces, and ends with '{last}'.")
  else:
    print(f"contains {characters} characters, {spaces} spaces, and ends with ''.")
  pass

check.set_print_exact("contains 17 characters, 2 spaces, and ends with '!'.")
check.expect("Example 1", analyze_string("Bananas are ripe!"), None)

check.set_print_exact("contains 0 characters, 0 spaces, and ends with ''.")
check.expect("Example 1", analyze_string(""), None)

