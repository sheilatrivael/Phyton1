import check
def concatenate(L: list[str]) -> str:
  """
  Returns the concatenation of all elements of L
  
  Examples:
     concatenate([]) => ''
     concatenate(['']) => ''
     concatenate(['b','a','n','a','n','a']) => 'banana'
  """
  answer = ''
  for pos in range(len(L)):
    answer += L[pos] 
  return answer
  pass
  
check.expect("Test3", concatenate(['b','a','n','a','n','a']), 'banana')
check.expect("Test1", concatenate([]), '')
check.expect("Test2", concatenate(['']), '')