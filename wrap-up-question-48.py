import check
def longest_string(t: tuple[str, ...]) -> str:
  """
  Returns the longest string
  
  Requires:
     len(t) > 0
  
  Examples:
     longest_string(("",)) => ""
     longest_string(("banana", "apple")) => "banana"
     longest_string(("banana", "apples")) => "banana"
  """
  
  longest = t[0]
  for i in range(1,len(t)) 
    if len(t[i]) > len(longest):
      longest  = t[i]
  return longest
  pass

check.expect("Test 1", longest_string(("",)), "")
check.expect("Test 2", longest_string(("banana", "apple")), "banana")
check.expect("Test 3", longest_string(("banana", "apples")), "banana") #both 6
check.expect("Test 4", longest_string(("banana", "bananas")), "bananas")