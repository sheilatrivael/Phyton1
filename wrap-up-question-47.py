import check
def find_all_subs(s: str, sub: str) -> tuple[int, ...]:
  """
  Returns a list of positions in s where sub can be found.

  Requires:
     sub != ''
  
  Examples:
     find_all_subs("", "a") => ()
     find_all_subs("aaa", "a") => (0, 1, 2)
     find_all_subs("banana", "an") => (1, 3)
  """
  
  pos = 0
  ct = ()
  while (s != "") and (pos < len(s)):
    if sub == s[pos:(pos+len(sub))]:  #(1:3) will check pos 1-2 if len(sub) = 2
      ct += (pos,)
    pos += 1
  return ct
  pass


check.expect("Test 1", find_all_subs("", "a"), ())
check.expect("Test 2", find_all_subs("aaa", "a"), (0, 1, 2))
check.expect("Test 3", find_all_subs("banana", "an"), (1, 3))
check.expect("Test 4", find_all_subs("banana", "ana"), (1, 3))
check.expect("Test 5", find_all_subs("banasanas", "anas"), (1, 5))