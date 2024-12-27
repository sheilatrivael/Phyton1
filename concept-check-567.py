import check
def rounder(L: list[list[float]]) -> None:
  """
  Mutates the list so the first occurrence of val is negated
  
  Effects: Mutates L
  
  Examples:
     L = []
     rounder(L) => None
     and L is not mutated
     
     L = [[0.3], [3.4,2.3,0.9], [], 
          [16.88,1.3333333,9.0,10.25], [0.51, 1.8887]]
     rounder(L) => None
     and L is mutated to:
     [[0], [3,2,1], [] ,[17,1,9,10], [1, 2]]
  """
  
  for row, M in enumerate(L):
    for col, _ in enumerate(M):
      L[row][col] = round(L[row][col])
  pass

##Examples:
L = []
check.expect("Ex 1 - empty list", rounder(L), None)
check.expect("Ex 1 Mutation", L, [])

L = [[0.3], [3.4,2.3,0.9], [], 
          [16.88,1.3333333,9.0,10.25], [0.51, 1.8887]]
check.expect("Ex 2 - singleton", rounder(L), None)
check.expect("Ex 2 Mutation", L, [[0], [3,2,1], [] ,[17,1,9,10], [1, 2]])