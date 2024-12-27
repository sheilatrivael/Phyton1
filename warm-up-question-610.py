import check
def multi_purpose(L: list[int]) -> int:
  """
  Mutates the list L so it is in reversed order,
  prints out the original list and returns
  the sum of the largest and smallest elements.
  
  Effects: 
     Prints to the screen
     Mutates L
  
  Requires: L is non-empty.
  
  Example:
    L = [1, 2, 3]
    multi_purpose(L) => 4
    L is mutated to [3, 2, 1] and [1, 2, 3] is printed.
  """

  M = L.copy()
  print(M)
  
  L.reverse()
  
  smallest = min(L)
  largest = max(L)
  return smallest + largest
  
  pass  


L = [1,2,3]
check.set_print_exact("[1, 2, 3]")
check.expect("Ex 1", multi_purpose(L), 4)
check.expect("Ex 1 Mutation", L, [3, 2, 1])