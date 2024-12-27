def echo():
  n = input("Enter a value:")
  print(n)

##Examples:
check.set_input("banana")
check.set_print_exact("banana")
check.expect("Example 1", echo(), None)