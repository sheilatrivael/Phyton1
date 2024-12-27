def n_times_no_loops():
  """
  Reads n from keyboard and prints n a total of n times
  once per line
  
  Effects: 
     Reads input from keyboard
     Prints to screen
  
  n_times_no_loops: None -> None
  
  Examples:
     If 0 is entered after 
     n_times_no_loops() => None
     is called, then nothing is printed.
  
     If 2 is entered after 
     n_times_no_loops() => None
     is called, then the following is printed:
     2
     2
     
  """
  n = input("Enter a integer:")
  s = int(n)
  if s > 0:
    print((n+"\n")*s, end="") #ensures no extra newline is added after the final print
  pass

#Test
check.set_input("0")
check.set_print_exact("")
check.expect("Test 0", n_times_no_loops(), None)

check.set_input("2")
check.set_print_exact("2", "2")
check.expect("Test 2", n_times_no_loops(), None)

check.set_input("3")
check.set_print_exact("3","3", "3")
check.expect("Test 3", n_times_no_loops(), None)

check.set_input("4")
check.set_print_exact("4", "4", "4", "4")
check.expect("Test 4", n_times_no_loops(), None)