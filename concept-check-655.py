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

  return [list(i) for i in zip(*L)]
  
  pass

check.expect("Test 1", transpose([]), [])
check.expect("Test 2", transpose([[1]]), [[1]])
check.expect("Test 3", transpose([[1, 2], [3, 4]]), [[1, 3], [2, 4]])