import check
def end_height(s: str) -> int:
  """
  Returns the last height starting from zero and going up for each 'u'
  character in s and down for every 'd' character in s.
  
  Requires:
     s consists of only 'u' and 'd' characters.
  
  Examples:
     end_height("") => 0
     end_height("uuuduu") => 4
     end_height("ddddud") => -4
     end_height("uuddu") => 1
  """
  
  u = s.count('u')
  d = s.count('d')
  return (u*1) + (d*-1)
  pass

check.expect("Test 0", end_height(""), 0)
check.expect("Test 1", end_height("uuuduu"), 4)
check.expect("Test 2", end_height("ddddud"), -4)
check.expect("Test 3", end_height("uuddu"), 1)