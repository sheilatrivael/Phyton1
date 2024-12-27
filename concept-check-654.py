import check
def make_tuples(n: int) -> list[tuple[int, int, int]]:
  '''
  Returns a list of tuples of the form
  [(0, 1, 2), (1, 2, 3), ..., (n, n+1, n+2)].
  
  Requires: n >= 0
  
  Examples:
     make_tuples(0) => [(0, 1, 2)]
     make_tuples(2) => [(0, 1, 2), (1, 2, 3), (2, 3, 4)]
  '''
  
  return list((a,a+1,a+2) for a in range(n+1))
  pass

check.expect("Test 1", make_tuples(0), [(0, 1, 2)])
check.expect("Test 2", make_tuples(2), [(0, 1, 2), (1, 2, 3), (2, 3, 4)])