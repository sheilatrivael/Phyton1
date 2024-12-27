import check
def nested_max(alol):
  '''
  Returns the largest value in alol
  
  nested_max: (listof (listof Int)) -> Int
  Requires: 
     alol is nonempty
     alol[0] is nonempty
  
  Examples:
     nested_max([[0], [1,2,3], [] ,[17,8,9,10]]) => 17
     nested_max([[1,5,3], [3],[35,1,2]]) =>  35
  '''
  
  current_max = alol[0][0]
  for L in alol:
    if L != []:
      for i in L:
        if i >= current_max:
          current_max = i
  return current_max

  pass

check.expect("Ex 1", nested_max([[0], [1,2,3], [] ,[17,8,9,10]]), 17)
check.expect("Ex 2", nested_max([[35,1], [200], [1,100]]), 200)
check.expect("Ex 3", nested_max([[1,100], [1],[35,1,2]]), 100)
check.expect("Ex 4", nested_max([[35,1], [1], [1,100]]), 100)
check.expect("Ex 5", nested_max([[1,5,3], [3],[35,1,2]]), 35)