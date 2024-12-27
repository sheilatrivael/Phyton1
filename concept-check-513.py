import check
def concatenate(L: list[str]) -> str:
  """
  Returns the concatenation of all elements of L
  
  Examples:
     concatenate([]) => ''
     concatenate(['']) => ''
     concatenate(['b','a','n','a','n','a']) => 'banana'
  """
  
  joined = "".join(L) #not "".join([L]), take out the [] so we join strings
  return joined
  pass

check.expect("Test 2", concatenate(['b','a','n','a','n','a']), 'banana')
check.expect("Test 0", concatenate([]), '')
check.expect("Test 1", concatenate(['']), '')
