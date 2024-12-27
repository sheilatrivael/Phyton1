import check
def rev_strings(los: list[str]) -> None:
  """
  Mutates los by reversing every element of los 
  in place and returns None
  
  Effects: Mutates los
  
  Examples:
     L = []
     rev_strings(L) => None
     and L is unchanged
     
     L = ['a', 'abc']
     rev_strings(L) => None
     and L is mutated to ['a', 'cba']
  """
  
  for pos, i in enumerate(los):
    if i != []: 
      los[pos] = los[pos][::-1]
  pass  

##Examples:
L = []
check.expect("Ex 1 - empty list", rev_strings(L), None)
check.expect("Ex 1 Mutation", L, [])

L = ['a', 'abc']
check.expect("Ex 2", rev_strings(L), None)
check.expect("Ex 2 Mutation", L, ['a', 'cba'])

L = ['banana']
check.expect("Ex 3", rev_strings(L), None)
check.expect("Ex 3 Mutation", L, ['ananab'])

L = ['aba']
check.expect("Ex 4", rev_strings(L), None)
check.expect("Ex 4 Mutation", L, ['aba'])