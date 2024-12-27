import check
def add_one(lon: list[int]) -> None:
  """
  Mutates lon by adding 1 to each element
  
  Effects: Mutates lon
  
  Examples:
     L = []
     add_one(L) => None
     and L is unchanged
     
     L = [1, 2, 3]
     add_one(L) => None
     and L is mutated to [2, 3, 4]
  """
  
  for pos in range(len(lon)):
    lon[pos] += 1
  pass

L = []
check.expect("Ex 1 - empty list", add_one(L), None) #L and lon will be aliases 
check.expect("Ex 1 Mutation", L, [])

L = [3]
check.expect("Ex 2 - singleton", add_one(L), None)
check.expect("Ex 2 Mutation", L, [4])

L = [1, 2, 3]
check.expect("Ex 3 - typical", add_one(L), None)
check.expect("Ex 3 Mutation", L, [2, 3, 4])

L = [10, -2, 3]
check.expect("T1 - 0 multiplier", add_one(L), None)
check.expect("T1 Mutation", L, [11, -1, 4])