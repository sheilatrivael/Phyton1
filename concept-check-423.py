import check
def halve_evens_ret(t: tuple[int, ...]) -> tuple[int, ...]:
  """
  Returns a copy of L with all even numbers divided by 2
  
  Examples:
     halve_evens_ret(()) => ()
     halve_evens_ret((1,3,5,7)) => (1,3,5,7)
     halve_evens_ret((1,2,3,4)) => (1,1,3,2)
  """
  
  pos = 0
  answer = ()
  
  if t == ():
    return answer
    
  while pos < len(t):
    if t[pos] % 2 == 0: #if even number, divided by 2 should have 0 remainder
      answer += (t[pos]//2,)
    else: #if odd number, return the number
      answer += (t[pos],)
    pos += 1
  return answer
  pass


check.expect("Test 0", halve_evens_ret(()), ())
check.expect("Test 1", halve_evens_ret((1,3,5,7)), (1,3,5,7))
check.expect("Test 2", halve_evens_ret((1,2,3,4)), (1,1,3,2))