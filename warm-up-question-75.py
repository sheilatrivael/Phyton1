import check
def sums(lol: list[list[int]]) -> None:
  '''
  Mutates lol so that each element is replaced by 
  the sum of the inner list
  
  Effects: Mutates lol
    
  Examples: 
     If L = [] then
     sums(L) => None
     and L is unchanged
     
     If L = [[]] then
     sums(L) => None
     and L is mutated to [0]
     
     If L = [[1, 2], [], [7, 8, 9, 10]] then
     sums(L) => None
     and L is mutated to [3, 0, 34]
  '''  
  
  for pos, inner in enumerate(lol):
    ans = 0
    for i in inner:
      ans += i
    lol[pos] = ans
      
  pass


L = [[1, 2], [], [7, 8, 9, 10]]
check.expect("Ex 2", sums(L), None)
check.expect("Ex 2 Mutation", L, [3, 0, 34])

L = [[]]
check.expect("Ex 1 - empty list", sums(L), None)
check.expect("Ex 1 Mutation", L, [0])

L = []
check.expect("Ex 1 - empty list", sums(L), None)
check.expect("Ex 1 Mutation", L, [])