import check
def non_inc(L: list[int]) -> bool:
  '''
  Returns True if the list L is non-increasing (decreasing)
  and False otherwise
  
  Examples:
     non_inc([]) => True
     non_inc([1]) => True
     non_inc([1, -1]) => True
     non_inc([1, 1]) => True
     non_inc([1, 2, 1]) => False
  '''
  
  M = list(map(lambda i: int(L[i] >= L[i+1]), range(len(L)-1)))
  if (sum(M) == len(L)-1) or (sum(M) > len(L)-1):
    return True
  return False
  
  pass


check.expect("Test 1", non_inc([]), True)
check.expect("Test 2", non_inc([1]), True)
check.expect("Test 3", non_inc([1, -1]), True)
check.expect("Test 4", non_inc([1, 1]), True)
check.expect("Test 5", non_inc([1, 2, 1]), False)
check.expect("Test 6", non_inc([3, 2, 1]), True)