import check
def a_phobic(s: str) -> str:
  '''
  Returns s without 'a's and if the number of 'a's removed was even,
  we also append a '!' character.
  
  Examples:
     a_phobic("") => "!"
     a_phobic("bananab") => "bnnb"
  '''
  
  copy_s = s[:]
  new_s = ""
  ct = 1
  
  for i in copy_s:
    if i == "a":
      i = ""
      ct += 1
    new_s += i
    
  if ct % 2 != 0: #if number of 'a' removed odd
      new_s += "!"
      
  return new_s
      
  pass

check.expect("Test 1", a_phobic("bananab"), "bnnb")
check.expect("Test 0", a_phobic(""), "!")
check.expect("Test 2", a_phobic("bananaba"), "bnnb!")