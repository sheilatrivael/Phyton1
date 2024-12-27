import check
def sum_average(L: list[list[int]]) -> None:
  """
  Mutates the list L so that it is sorted in increasing order of sum 
  with ties broken by the decreasing average of the numbers in the list.
    
  Effects: Mutates L
  
  Requires: L[i] != [] for each 0 <= i < len(L)
  
  Examples:
     If L = [] then
     sum_average(L) => None
     and L is unchanged
     
     If L = [[1,0,0,0,0], [1,0,0,0]] then
     sum_average(L) => None
     and L is mutated to [[1,0,0,0], [1,0,0,0,0]]
     
     If L = [[3, 1, 8], [12]] then
     sum_average(L) => None
     and L is mutated to [[12], [3, 1, 8]]
     
     If L = [[3, 1, 8], [100, 1000, 10000] , [2, 3, 4]] then
     sum_average(L) => None
     and L is mutated to [[2, 3, 4], [3, 1, 8], [100, 1000, 10000]]
  """

  L.sort(key = lambda x: (sum(x), len(x)))
  pass

L = [[3, 1, 8], [100, 1000, 10000] , [2, 3, 4]]
check.expect("Ex 4", sum_average(L), None)
check.expect("Ex 4 Mutation", L, [[2, 3, 4], [3, 1, 8], [100, 1000, 10000]])

L = []
check.expect("Ex 1 - empty list", sum_average(L), None)
check.expect("Ex 1 Mutation", L, [])

L = [[1,0,0,0,0], [1,0,0,0]]
check.expect("Ex 2", sum_average(L), None)
check.expect("Ex 2 Mutation", L, [[1,0,0,0], [1,0,0,0,0]])

L = [[3, 1, 8], [12]]
check.expect("Ex 3", sum_average(L), None)
check.expect("Ex 3 Mutation", L, [[12], [3, 1, 8]])

