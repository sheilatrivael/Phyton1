import check
def course_grade(warmup: int, inlec: int, wrapup: int,
                         assigs: int , final: int) -> int:
  """
  Returns your course grade
  
  Requires: 
     0 <= warmup, inlec, wrapup, assigs, final <= 100
  
  Examples:
     course_grade(100, 100, 100, 100, 100) => 100
     course_grade(0, 0, 0, 0, 0) => 0
     course_grade(80, 80, 80, 80, 70) => 78
  """
  
  total_grade = (warmup*0.05) + (inlec*0.1) + (wrapup* 0.05) + (assigs*0.6) + (final*0.2) 
  return int(round(total_grade, 0))
  pass

check.expect ("Test 1", course_grade(100, 100, 100, 100, 100), 100)
check.expect ("Test 2", course_grade(0, 0, 0, 0, 0), 0)
check.expect ("Test 3",course_grade(80, 80, 80, 80, 70), 78)