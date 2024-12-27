import check
def max_even_sum(lol: list[list[int]]) -> int:
  """
  Returns the sum of the even integers in the inner list in lol 
  that has the maximal even integer sum
  
  Requires: lol is non-empty
  
  Examples:
     max_even_sum([[]]) => 0
     max_even_sum([[], [3], [10,1,3,5,7], [2,4,6]]) => 12
     max_even_sum([[1,3,5,7],[-10]]) => 0
  """
  
  max_sum = 0 #set the sum of the first list
  for i in lol[0]:
    if i % 2 == 0:  #check if the number is even (and non-negative?)
      max_sum += i  #if even, add to ans
    
  #after finish checking one inner list, check if current max changed    
  for inner_list in lol:
    
    current_sum = 0
    for i in inner_list:
      if i % 2 == 0:
        current_sum += i
    
    if current_sum > max_sum:
      max_sum = current_sum
  
  return max_sum
  
  pass

check.expect("Ex 1", max_even_sum([[]]), 0)
check.expect("Ex 3", max_even_sum([[], [3], [10,1,3,5,7], [2,4,6]]), 12)
check.expect("Ex 4", max_even_sum([[1, 3, 5, 7], [-10]]), 0)
