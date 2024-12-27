import check
from typing import Tuple, Any
def reversed_multiple_tuple(t: tuple, start: int, k: int) -> tuple:
  """
  Returns a reverse of every kth element in t 
  starting with start (zero indexed)
  
  Requires: 
     0 <= start
     0 < k
  
  Examples:
     reversed_multiple_tuple((), 0, 1) => ()
     reversed_multiple_tuple((1,2,3,4,5,6,7,8,9), 2, 5) => (8, 3)
  """
  
  sliced = t[start::k]
  reversed = sliced[::-1]
  return reversed
  pass


check.expect("Test2", reversed_multiple_tuple((1,2,3,4,5,6,7,8,9), 2, 5), (8, 3))
check.expect("Test1", reversed_multiple_tuple((), 0, 1), ())