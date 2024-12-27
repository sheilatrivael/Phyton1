import check
def halve_evens_ret(L: list[int]) -> list[int]:
  """
  Returns a copy of L with all even numbers divided by 2
  
  Examples:
     halve_evens_ret([]) => []
     halve_evens_ret([1,3,5,7]) => [1,3,5,7]
     halve_evens_ret([1,2,3,4]) => [1,1,3,2]
  """
  pos = 0
  ans = []
  while pos < len(L) and L != []:
    if L[pos] % 2 == 0: #if it's even numbers
      ans.append(L[pos] // 2)
    else:
      ans.append(L[pos])
    pos += 1
  return ans
  pass

check.expect("Test 1", halve_evens_ret([]), [])
check.expect("Test 2", halve_evens_ret([1,3,5,7]), [1,3,5,7])
check.expect("Test 3", halve_evens_ret([1,2,3,4]), [1,1,3,2])