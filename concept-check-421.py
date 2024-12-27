import check
def tuple_score(t: tuple) -> int:
  '''
  Returns the score of t where strings count as 1 point,
  integers count as their value and other types are worth 0.
  
  Examples:
     tuple_score(()) => 0
     tuple_score(("1", 1, True, (1,2,3))) => 2
     tuple_score(("bigword!!!", 99)) => 100
  '''
  
  answer = 0
  while t != (): 
    if type(t[0]) == str:
      answer += 1  
    elif type(t[0]) == int: #if alphabet or number
      answer += int(t[0])
    t = t[1:]
  return answer
  pass


check.expect("Example 1", tuple_score(()), 0)
check.expect("Example 2", tuple_score(("1", 1, True, (1,2,3))), 2)
check.expect("Example 3", tuple_score(("bigword!!!", 99)), 100)