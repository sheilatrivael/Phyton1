import check
def grade(mark):
  if 80 <= mark <= 100:
    return 'A'
  if 70 <= mark <= 79:
    return 'B'
  if 60 <= mark <= 69:
    return 'C'
  if 50 <= mark <= 59:
    return 'D'
  if mark < 50:
    return 'F'
    
def convert_to_letter_grade(lon: list[int]) -> list[str]:
  '''
  Returns a new list where each value in lon
  is replaced by a letter grade
  
  Requires: 0 <= L[i] <= 100 for each 0 <= i <= len(L)
  
  Examples:
     convert_to_letter_grade([]) => []
     convert_to_letter_grade([0]) => ['F']
     convert_to_letter_grade([49, 59, 69, 79, 89]) 
        => ['F', 'D', 'C', 'B', 'A']
  '''
  
  M = list(map(grade, lon))
  return M
  
  pass
    
check.expect("Test 3", convert_to_letter_grade([49, 59, 69, 79, 89]), ['F', 'D', 'C', 'B', 'A'])    
check.expect("Test 2", convert_to_letter_grade([0]), ['F'])
check.expect("Test 1", convert_to_letter_grade([]), [])