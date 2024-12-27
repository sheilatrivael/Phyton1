def max_digit(n: int) -> int:
  """
  Returns the largest digit of the two digit number n
  
  Requires: 10 <= n <= 99
  
  Examples:
     max_digit(10) => 1
     max_digit(99) => 9
  """
  #YOUR CODE GOES HERE
  a = n // 10
  b = n % 10
  return max(a,b)
  pass

max_digit(10)
max_digit(99)
max_digit(19)