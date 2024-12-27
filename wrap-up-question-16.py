def reverse(n: int) -> int:
  """
  Returns the two-digit natural number n in reverse order
  
  Requires: 10 <= n <= 99
  
  Examples:
     reverse(10) => 1
     reverse(34) => 43
     reverse(99) => 99
  """
  
  ##YOUR CODE GOES HERE
  first = n // 10
  second = n % 10
  reversed = int(str(second) + str(first))
  return reversed
  pass

reverse(43)
reverse(97)
reverse(66)