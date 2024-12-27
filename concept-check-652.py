import check
def transpose(L: list[list[int]]) -> list[list[int]]:
  '''
  Returns the transpose of L
  
  Requires: len(L[i]) are equal for all 0 <= i < len(L)
  
  Examples:
     transpose([]) => []
     transpose([[1]]) => [[1]]
     transpose([[1, 2], [3, 4]]) => [[1, 3], [2, 4]]
  '''
  
  #number of row = column
  #L[0] is the  first row in the matrix [1,2]
  #len(L[0]) will give the number of column = 2
  #iterate through column 0,1 until < 2
  M = [ [L[row][column] for row in range(len(L)) ] \
      for column in range(len(L[0]))] if L else []
  return M
  
  pass



check.expect("Test 1", transpose([]), [])
check.expect("Test 2", transpose([[1]]), [[1]])
check.expect("Test 3", transpose([[1, 2], [3, 4]]), [[1, 3], [2, 4]])

