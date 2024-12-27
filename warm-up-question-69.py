import check
def halve_evens(L: list[int]) -> None:
  """
  Returns None and mutates L so that all even numbers are halved
  
  Effects: Mutates L
  
  Examples:
     L = []
     halve_evens(L) => None
     and L is still []
     
     L = [1,3,5,7]
     halve_evens(L) => None
     and L is still [1,3,5,7]
     
     L = [1,2,3,4]
     halve_evens(L) => None
     and L has been mutated to [1,1,3,2]
  """
  pos = 0
  while pos < len(L) and L != []:
    if L[pos] % 2 == 0: #if it's even numbers
      L[pos] = L[pos] // 2
    pos += 1
  pass

L = []
check.expect("Ex 1 - empty list", halve_evens(L), None)
check.expect("Ex 1 Mutation", L, [])

L = [1,3,5,7]
check.expect("Ex 2", halve_evens(L), None)
check.expect("Ex 2 Mutation", L, [1,3,5,7])

L = [1,2,3,4]
check.expect("Ex 3", halve_evens(L), None)
check.expect("Ex 3 Mutation", L, [1,1,3,2])
