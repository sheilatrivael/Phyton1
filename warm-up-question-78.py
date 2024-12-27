import check
def equinumerous(s: str) -> bool:
  '''
  Returns True if s is equinumerous and False otherwise.
  
  Examples:
     equinumerous("0") => False
     equinumerous("1010") => True
  '''
  
  d = {"0":0, "1":0}
  
  for i in s:
    if i == "0":
      d["0"] += 1
    if i == "1":
      d["1"] += 1

  return d["0"] == d["1"]
  pass

check.expect("Test 0", equinumerous("0"), False)
check.expect("Test 1", equinumerous("1010"), True)