import check
def first_digits(L: list[int]) -> None:
  """
  Mutates L so that each element is replaced by the first digit
  
  Effects: Mutates L
  
  Requires: L[i] > 0 for all indices i.
  
  Examples:
     If L is [] then
     first_digits(L) => None
     and L is unchanged
     
     If L is [31, 13] then
     first_digits(L) => None
     and L is mutated to [3, 1]
     
     If L is [1, 2, 3] then
     first_digits(L) => None
     and L is unchanged
  """
  
  for i in range(len(L)):
    if (L[i] // (10 ** (len(str(L[i])) - 1))) != 0:
      L[i] = L[i] // (10**(len(str(L[i]))-1))
  pass

##Examples:
L = []
check.expect("Ex 1 - empty list", first_digits(L), None)
check.expect("Ex 1 Mutation", L, [])

L = [31, 13]
check.expect("Ex 2", first_digits(L), None)
check.expect("Ex 2 Mutation", L, [3, 1])

L = [1, 2, 3]
check.expect("Ex 3", first_digits(L), None)
check.expect("Ex 3 Mutation", L, [1, 2, 3])

L = [111, 222, 333]
check.expect("Ex 4", first_digits(L), None)
check.expect("Ex 4 Mutation", L, [1, 2, 3])

L = [1111, 2222, 3333]
check.expect("Ex 4", first_digits(L), None)
check.expect("Ex 4 Mutation", L, [1, 2, 3])