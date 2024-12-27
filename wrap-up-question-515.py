import check
def repel(los: list[str], char: str) -> int:
  """
  Mutates los by removing every element 
  of the list of strings los that
  contains char and returns the total
  number of elements mutated.
  
  Effects: Mutates los
  
  Requires: len(char) == 1
  
  Examples:
     L = []
     repel(L, 'a') => 0
     and L is unchanged
     
     L = ['a', 'abc']
     repel(L, 'b') => 1
     and L is mutated to ['a', '']
  """
  
  pos = 0
  ct = 0
  for i in los:
    if char in i and (pos < len(los)):
      los[pos] = ''
      ct += 1
    pos += 1
    
  return ct
  pass

##Examples:
L = ['a', 'abc']
check.expect("Ex 2", repel(L, 'b'), 1)
check.expect("Ex 2 Mutation", L, ['a', ''])

L = []
check.expect("Ex 1 - empty list", repel(L, 'a'), 0)
check.expect("Ex 1 Mutation", L, [])