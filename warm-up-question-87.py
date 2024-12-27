import check
def collate(t: tuple[str]) -> tuple[str]:
  """
  Returns a tuple of strings where the answer at each index
  i is formed by using all the ith letters from strings of t

  Examples:
     collate(()) => ()
     collate(("a",)) => ("a",)
     collate(("tee", "ear", "ate")) => ("tea", "eat", "ere")
  """
  
  if t == ():
    return ()
    
  ans = []
 
  for pos in range(len(t[0])): #pos = 0
    new = "".join(word[pos] for word in t)
    ans.append(new)
      
  return tuple(ans)
      

  pass

check.expect("Test 3", collate(("tee", "ear", "ate")), ("tea", "eat", "ere"))
check.expect("Test 2", collate(("a",)), ("a",))
check.expect("Test 1", collate(()), ())


"""
note to myself:
Iterate over the range of string length (which is the same for all strings in the tuple).
Collect characters from each string at the current index and form a new string.
Return a tuple of these strings.
"""