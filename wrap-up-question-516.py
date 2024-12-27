import check
def negate_first(L: list[list[int]], val: int):
  '''
  Mutates the list so the first occurrence of val is negated
  
  Effects: Mutates L
  
  Requires: 
     val occurs in L and is positive
  
  Examples:
     L = []
     negate_first(L, 10) => None
     and L is not mutated
     
     L = [[0], [3,2,1], [] ,[17,1,9,10], [1, 2]]
     negate_first(L, 1) => None
     and L is mutated to:
     [[0], [3,2,-1], [] ,[17,1,9,10], [1, 2]]
  '''
  
  for M in L:
    for pos, i in enumerate(M):
      if i == val:
        M[pos] = val*(-1)
        return
  pass



##Examples:
L = [[0], [3,2,1], [] ,[17,1,9,10], [1, 2]]
check.expect("Ex 2", negate_first(L, 1), None)
check.expect("Ex 2 Mutation", L, [[0], [3,2,-1], [] ,[17,1,9,10], [1, 2]])

L = []
check.expect("Ex 1 - empty list", negate_first(L, 10), None)
check.expect("Ex 1 Mutation", L, [])