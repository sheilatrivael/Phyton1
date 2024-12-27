import check
def swap_two(s: str, pos1: int, pos2: int) -> str:
  """
  Returns s with s[pos1] and s[pos2] swapped.
  
  Requires:
     len(s) >= 2
     0 <= pos1 <= len(s) - 1
     0 <= pos2 <= len(s) - 1
  
  Examples:
     swap_two("ab", 0, 1) => "ba"
     swap_two("banana", 2, 5) => "baaann"
  """
  
  a = s[pos1:(pos1+1)]
  b = s[pos2:(pos2+1)]
  if a != b:
    change1 = s[:pos1] + b + s[(pos1+1):] 
    change2 = change1[:pos2] + a + change1[(pos2+1):]
    return change2
  else:
    return s
  pass

#Typical values
check.expect("Test 1", swap_two("banana", 2, 5), "baaann")

#Small and large values
check.expect("small", swap_two("ab", 0, 1), "ba")
check.expect("large", swap_two("incomprehensibilities", 0, 20), "sncomprehensibilitiei")
check.expect("large swap", swap_two("a" * 1000, 100, 999), "a" * 1000)

#Boundary values and 
check.expect("first and last", swap_two("banana", 0, 5), "aananb")
check.expect("first", swap_two("banana", 0, 0), "banana")
check.expect("last", swap_two("banana", 5, 5), "banana")

#Special cases
check.expect("same letter", swap_two("banana", 1, 3), "banana")
check.expect("same letter", swap_two("banana", 3, 3), "banana")
check.expect("pos1 larger", swap_two("banana", 5, 2), "baaann") #important

#Relationship between parameters
check.expect("same spot", swap_two("banana", 1, 1), "banana")