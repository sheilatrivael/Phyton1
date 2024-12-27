import check
def two_ending_cubes(a: int, b: int) -> set[int]:
  '''
  Returns a set of all cubes ending with a 2 between a and b inclusive
  
  Examples:
     two_ending_cubes(0, 0) -> set({})
     two_ending_cubes(-8, 9) -> {8, -8}
  '''
  
  if a > b:
    return set()
  else:
    return {x for x in range(a,b+1) if abs((x**3)) % 10 == 2}
  pass

check.expect("Test 1", two_ending_cubes(0, 0), set({}) )
check.expect("Test 2", two_ending_cubes(-8, 9), {8, -8} )
check.expect("Test 2", two_ending_cubes(9, -8), set({}))