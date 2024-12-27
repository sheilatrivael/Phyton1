import check
def n_times() -> None:
  """
  Reads n from keyboard and prints n a total of n times
  once per line
  
  Effects: 
     Reads input from keyboard
     Prints to screen
  
  Examples:
     If 0 is entered after 
     n_times() => None
     is called, then nothing is printed.
  
     If 2 is entered after 
     n_times() => None
     is called, then the following is printed:
     2
     2
     
  """
  n = input("Enter a integer:")
  s = int(n)
  while s > 0:
    print(n)
    s = s - 1
  pass

#Test
check.set_input("0")
check.set_print_exact("")
check.expect("Test 0", n_times(), None)

check.set_input("2")
check.set_print_exact("2", "2")
check.expect("Test 2", n_times(), None)

check.set_input("2")
check.set_print_exact("2\n2")
check.expect("Test 2", n_times(), None)

check.set_input("2")
check.set_screen("Prints 2 on two separate lines")
check.expect("Test", n_times(), None)

check.set_input("3")
check.set_print_exact("3", "3", "3")
check.expect("Test 3", n_times(), None)

check.set_input("4")
check.set_print_exact("4", "4", "4", "4")
check.expect("Test 4", n_times(), None)
