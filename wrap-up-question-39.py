import check
def sum_triples() -> None:
  """
  Consumes 3 integer inputs from keyboard
  and prints the sum of the three integers
  
  Effects:
     Prints to screen
     Reads input from keyboard
  
  Examples:
     If we call
     sum_triples() => None
     and give integers 1, 2, 3 as input,
     we print "6" to the screen (no quotes)
  """
  a = int(input("Enter the first integer: "))
  b = int(input("Enter the second integer: "))
  c = int(input("Enter the third integer: "))
  print(a+b+c)
  pass


check.set_input("1", "2", "3")
check.set_print_exact("6")
check.expect("Test 0", sum_triples(), None)