import check
def repeat() -> None:
  """
  Requests a string and an integer from keyboard
  and repeats the string the integer number of times
  and prints to the screen
  
  Effects:
     Prints to the screen
     Reads input from keyboard
  
  Examples:
     repeat() => None
     
     and abcabcabc is printed assuming the input given is
     abc
     3
     in that order.
  """
  
  s = input("Enter a string: ")
  n = input("Enter a positive integer: ")
  print(s*int(n))
  pass

check.set_input("abc", "3")
check.set_print_exact("abcabcabc")
check.expect("Test 0", repeat(), None)