import check
def swap(L: list, pos1: int, pos2: int) -> None:
  """
  Swaps L[pos1] and L[pos2]
  
  Effects: Mutates L
  
  0 <= pos1, pos2 < len(L)
  
  Examples:
     L = [1, 2]
     swap(L, 0, 1) => None
     and L is mutated to [2, 1]
  """

  
  A = L[pos1]
  B = L[pos2]
  L[pos1] = B
  L[pos2] = A
  pass


L = [1, 2]
check.expect("Ex 1", swap(L, 0, 1), None) #L and lon will be aliases 
check.expect("Ex 1 Mutation", L, [2, 1])

L = [3, 3]
check.expect("Ex 2", swap(L, 0, 1), None)
check.expect("Ex 2 Mutation", L, [3,3])

L = [1, 2, 3, 4, 5]
check.expect("Ex 3", swap(L, 0, 4), None)
check.expect("Ex 3 Mutation", L, [5, 2, 3, 4, 1])

L = [1, 2, 3, 4, 5]
check.expect("Ex 4", swap(L, 1, 3), None)
check.expect("T1 Mutation", L, [1, 4, 3, 2, 5])