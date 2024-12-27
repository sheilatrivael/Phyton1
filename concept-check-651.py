import check
def odd_dictionary(n: int) -> dict[int, int]:
  '''
  Returns a dictionary where each key:value pair
  is of the form i:2*i+1
  
  Requires: 0 <= n
  
  Examples:
     odd_dictionary(0) => {0:1}
     odd_dictionary(2) => {0:1, 1:3, 2:5}
  '''
  
  return {i: 2*i+1 for i in range(n+1)}
  
  pass

check.expect("Test 1", odd_dictionary(0), {0:1})
check.expect("Test 2", odd_dictionary(2), {0:1, 1:3, 2:5})