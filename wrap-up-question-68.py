import check
def sum_columns(t):
  '''
  Returns a list consisting of the sum of all columns of Table t
  where Tables are (listof (listof Int)).
  
  sum_columns: Table -> (listof Int)
  
  Examples:
     sum_columns([[1]]) => [1]
     sum_columns([[1,2,3]]) => [1, 2, 3]
     sum_columns([[1],[2],[3]]) => [6]
     sum_columns([[1,2],[3,4],[5,6],[7,8]]) => [16, 20]
  '''
  
  #transpose zip
  L = [list(i) for i in zip(*t)]

  #L = [[1,3,5,7] , [2,4,6,8]]
  total = list(map(sum, L))
  return total
  
  pass

check.expect("Test 4", sum_columns([[1,2],[3,4],[5,6],[7,8]]), [16, 20])
check.expect("Test 1", sum_columns([[1]]), [1])
check.expect("Test 2", sum_columns([[1,2,3]]), [1, 2, 3])
check.expect("Test 3", sum_columns([[1],[2],[3]]), [6])

"""
  #transpose Concept Check 6.5.2
  L = [ [t[row][column] for row in range(len(t)) ] \
      for column in range(len(t[0]))] if t else []
"""
