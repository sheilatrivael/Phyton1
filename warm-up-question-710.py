import check
def make_list(n: int) -> list[str]:
  '''
  Returns the list of strings formed by in position n, 
  repeating n a total of n times
  
  Requires: n >= 0
  
  Examples:
     make_list(0) => ['']
     make_list(3) => ['', '1', '22', '333']
  '''
  
  ans = ['']
  
  for i in range(n):
    L = ans.append(str(i+1)*(i+1))
  return ans

  pass

check.expect("Test 0", make_list(0), [''])
check.expect("Test 2", make_list(2), ['', '1', '22'])
check.expect("Test 3", make_list(3), ['', '1', '22', '333'])