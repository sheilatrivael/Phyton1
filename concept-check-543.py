import check
def str_starters_list(L: list[str], s: str) -> int:
  """
  Returns the number of all elements in 
  L that start with s
  
  Examples: 
     str_starters_list([], '') => 0
     str_starters_list(['banana', 'bar', 
                  'blast', 'bag', 'apple', 'zoo'], 'ba') => 3
  """
  
  answer = 0
  for pos in range(len(L)):
    if L[pos].startswith(s) == True:
      answer += 1
  return answer
  pass

check.expect("Test 0", str_starters_list(['banana', 'bar', 
                  'blast', 'bag', 'apple', 'zoo'], 'ba'), 3)
check.expect("Test 0", str_starters_list([], ''), 0)